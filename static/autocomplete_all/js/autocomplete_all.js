/*
This is workaround for pure behaviour of autocomplete_fields in Django (2,3).
Probably you cannot modify the native Django ajax url (../autocomplete/) and you can only access the Referer url.

Lets say, you have 2 <select>s with same ForeignKey (example: User).
In such case you cannot identify on the server-side (in get_search_results) which one <select> is active.
This trick will extend the Referer url to give more info to the server-side.
Basically ?key=<fieldname> will be added to identify the <select>
    but you can add more (see bellow) and implement dynamic filters (dependent on current form values) too.

EXAMPLE:
this is automatically called: source ModelAdmin, class Media, js = ('autocomplete_all/js/autocomplete_all.js',)
target ModelAdmin:
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.is_ajax and '/autocomplete/' in request.path:
            url = urllib.parse.urlparse(request.headers['Referer'])
            referer = url.path
            qs = urllib.parse.parse_qs(url.query)
            if '/npo/finding/' in referer:            # /<app>/<model>/
                if qs.get('key') == ['id_process']:   # <field ~ foreignkey> (parse_qs results are lists)
                    queryset = queryset.filter(...)
        return queryset, use_distinct
*/

/* I leave this, not able make the fake Admin working outside of Admin */
// /* Django native admin/js/autocomplete.js depends on presence of django.jQuery.
//    Outside of Admin, if this .js is called before autocomplete.js, following will make possible autocomplete.js to work.
//    This is skipped inside Admin where django.jQuery exists.
// */
// if (typeof(django) === "undefined") {
//     django = {};
// }
// if (typeof(django.jQuery) === "undefined") {
//     django.jQuery = $;
// }

document.addEventListener("DOMContentLoaded", function () {
    (function ($) {
        $('select.admin-autocomplete').on('select2:opening', function (evt) {
            if (!window.history.orig_pathname) {
                window.history.orig_pathname = window.location.pathname;
            }
            this.modified_location_search_key = '?key=' + this.id;
            this.modified_location_search = this.modified_location_search_key + expand_ajax_params($, this.id);
            window.history.replaceState(null, null, window.history.orig_pathname + this.modified_location_search);
        });
        $('select.admin-autocomplete').on('select2:closing', function (evt) {
            var keypart = (window.location.search + '&').split('&', 1)[0];
            if (keypart === this.modified_location_search_key) {  // opening of new runs earlier of closing the old one :(
                window.history.replaceState(null, null, window.history.orig_pathname);
            }
        });
    })(django.jQuery || $);
});

/*
If you need dynamic filter based on some current value of other field in your admin form then:
You can add second (yours) ModelAdmin Media js file and there rewrite the function expand_ajax_params.
Example:
In ModelAdmin, class Media: js = ('autocomplete_all/js/autocomplete_all.js', <myapp>/js/autocomplete_asset.js)
In autocomplete_asset.js:
function expand_ajax_params($, key) {
    if (key === 'id_asset') {          // we need dynamic filtering with 'asset' foreignkey only
        return '&city=' + $('#id_city').val() + &country=' + $('#id_country').val();   // ie. give only assets from London+UK
    } else {
        return ''
    }
}
(Or you could make it easier and give parameters always regardless on the current <select>:
    just remove the if/else and use the 1st return only.)
*/

// the default function adds nothing to params (except of ?key=..)
//  but you can rewrite this function in particular js file (entered as 2nd one in Source admin, class Media, js=(.., ..))
function expand_ajax_params($, fieldId) {
    function sanitize(string) {  // https://stackoverflow.com/questions/2794137/sanitizing-user-input-before-adding-it-to-the-dom-in-javascript
        if (string === null) {return '';}

        // https://stackoverflow.com/questions/4310535/how-to-convert-anything-to-a-string-safely-in-javascript
        switch (typeof string) {
            case 'object':
                return 'object';
            case 'function':
                return 'function';
            default:
                return string + '';  // to string (dj 3.2 was reported an issue with non-string content here, which fails on string.replace)
        }

        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#x27;',
            "/": '&#x2F;',
        };
        const reg = /[&<>"'/]/ig;
        return string.replace(reg, (match)=>(map[match]));
    }
    let controls = $('input, select');
    let textareas = $('textarea');
    let expanded = '';
    for (let i = 0; i < controls.length; i++) {
        expanded += '&' + controls[i].name + '=' + sanitize($(controls[i]).val());
    }
    for (let i = 0; i < textareas.length; i++) {
        let content = $(textareas[i]).val();
        expanded += '&' + textareas[i].name + '=' + content.length;   // for textareas ie. can be tested ==='0', !=='0'
        if (content.length <= 40) {expanded += ':' + sanitize(content);}      // the short content is also accessible
    }
    return expanded;
    // return '&country=' + $('#id_country').val();
}
