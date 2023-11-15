from django.contrib import auth
from django.contrib.auth import load_backend
from django.contrib.auth.backends import RemoteUserBackend
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import requests
from anmaabankApp.models import *

def getUrl(request):
    if request is None:
        raise Exception("request is None")

    return request.build_absolute_uri()


def set_test_cookie(request, render, key_cookies):
    render.set_cookie("sessionid", key_cookies,
                      max_age=10000000, expires=10000000)
    request.session['session_cookies'] = key_cookies


def set_cookie_page(request, render, url,):
    import random
    import string
    rend = HttpResponse(request, 'index.html')
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(100))
    # req = request
    if request.COOKIES.get(url.replace(".", "").replace("/", "").replace(":", ""),) == '':
        
        render.set_cookie(url.replace(".", "").replace("/", "").replace(":", ""), result_str,
                        max_age=10000000, expires=10000000)
        request.session[url.replace(".", "").replace(
            "/", "").replace(":", "")] = result_str

def get_user_admin(request):
    if not hasattr(request, "_cached_user"):
        request._cached_user = auth.get_user(request)
    return request._cached_user


def check_cookie(request, render, key_cookies):
    # print(request.COOKIES.get('csrftoken'))
    # # print(request.session['session_cookies'])
    cookis = request.COOKIES.get('sessionid')
    # print(request.COOKIES.get('cookies'))
    # print(cookis)
    # session = request.session()
    if cookis != None:
        # print(request.session.get('sessionid'))
        request.session.set_expiry(10000000)

        # render.cookies['cookies']['expires'] = datetime.today() + \
        #     timedelta(days=1000)
        # render.cookies['cookies']['expires'] = datetime.today() + \
        #     timedelta(days=1000)
        # request.session.delete_test_cookie()
        # print(request.session.get_session_cookie_age())

        cookis = request.COOKIES.get('sessionid')

    else:
        set_test_cookie(request, render, key_cookies)
        # render.updte.set_expiry(10000000)
        request.session.set_expiry(10000000)
    # print(request.COOKIES.get('cookies'))
    # print(request.COOKIES)
    # request.COOKIES['cookies']['expires'] = 10000000

    cookis = request.COOKIES.get('sessionid')

    # response = HttpResponse(
    #     "Dataflair <br> Your browser doesnot accept cookies")
    return cookis


def get_cookie(request):
    import random
    import string
    rend = HttpResponse(request, 'index.html')
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(100))
    req = request
    # set_cookie_page(req, rend, result_str)
    sessi = check_cookie(req, rend, result_str)
    if sessi == None:
        sessi = result_str
        set_test_cookie(req, rend, result_str)
        sessi = check_cookie(req, rend, result_str)
    return sessi


def get_clients_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_clients_ipss(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def saveInfoIp(request, screen):
    if request.method == 'GET':
        cookie = get_cookie(request)

        try:
            print("start: http: // ip-api.com/json/{0}".format(get_clients_ip(request)))
            response = requests.get(
                'http://ip-api.com/json/{0}'.format(get_clients_ip(request))).json()
            print(
                "end: http: // ip-api.com/json/{0}".format(get_clients_ip(request)))

            result = {}
            result = response
            print(type(result))
            print(result)

            # print(result)
            if result['status'] != 'fail':
                ip_info = IpInfo.objects.create(
                    status=result['status'],
                    ip=result['query'],
                    latitude=result['lat'],
                    longitude=result['lon'],
                    isp=result['isp'],
                    screen=screen,
                    url_google_map_location="https://www.google.com/maps?q=" +
                    str(result['lat'])+","+str(result['lon']),
                    cookie=cookie,
                    COOKIES=cookie,
                    regionCode=result['region'],
                    countryCode=result['countryCode'],
                    country=result['country'],
                    regionName=result['regionName'],
                    city=result['city'],
                    zip=result['zip'],
                    timezone=result['timezone'],
                    asn=result['as'],
                    org=result['org'],
                )
                saveInfoReqestHeder(request, screen, cookie, ip_info)
            else:
                ip_info = IpInfo.objects.create(ip=result['query'],
                                                status=result['status'],

                                                #   latitude=result['lat'],
                                                #   longitude=result['lon'],
                                                #   isp=result['isp'],
                                                screen=screen,
                                                cookie=cookie,
                                                COOKIES=cookie,
                                                #   regionCode=result['region'],
                                                #   countryCode=result['countryCode'],
                                                #   country=result['country'],
                                                #   regionName=result['regionName'],
                                                #   city=result['city'],
                                                #   zip=result['zip'],
                                                #   timezone=result['timezone'],
                                                #   asn=result['as'],
                                                #   org=result['org'],
                                                )
                saveInfoReqestHeder(request, screen, cookie, ip_info)

        except ValueError as e:
            print("ValueError "+str(e))
        except requests.exceptions.ConnectionError as e:
            print("requests exceptions ConnectionError "+str(e))
        except Exception as e:
            print("requests exception  "+str(e))


def saveInfoReqestHeder(request, fromUrl, cookie, ip_info):
    print(request.META)
    # print(request.path)
    # print(request.META)
    # print(type(request.META))
    # print(type(request.headers))
    # print(request.method)
    # print("path")
    # print(request.headers)
    import json

    # for jjjj in request.META:
    # print(jjjj)

    # print(
    # json.dumps(request.GET)
    # )

    try:
        data_json = request.META
        my_dictss = {
            # 'body': request,
            'fromUrl': fromUrl,
            "Meta": str(request.META)
            # "META": request.META.items()
            # 'META': {k.lower(): v for (k, v) in request.META}
        }
        # my_dictsssss = {
        #     # 'body': request,
        #     'fromUrl': fromUrl,
        #     # "get": str(request.GET)
        #     'GET': json.dumps({k.lower(): v for (k, v) in request.GET})

        #     # "META": request.META.items()
        #     # 'META': {k.lower(): v for (k, v) in request.META}
        # }
        # .get("https://www.python.org/")
        RequestMetaAndGet.objects.create(
            datajson=my_dictss,
            datajsonGet=json.dumps(request.GET),
            PATH=request.path,
            cookie=cookie,
            # COOKIES=cookie,
            ip_info=ip_info,
            CONTENT_LENGTH=request.META.get("CONTENT_LENGTH", ''),
            CONTENT_TYPE=request.META.get("CONTENT_TYPE", ''),
            HTTP_ACCEPT=request.META.get("HTTP_ACCEPT", ''),
            HTTP_ACCEPT_ENCODING=request.META.get("HTTP_ACCEPT_ENCODING", ''),
            HTTP_ACCEPT_LANGUAGE=request.META.get("HTTP_ACCEPT_LANGUAGE", ''),
            HTTP_HOST=request.META.get("HTTP_HOST", ''),
            HTTP_REFERER=request.META.get("HTTP_DNT", ''),
            HTTP_USER_AGENT=request.META.get("HTTP_USER_AGENT", ''),
            # PATH=request.META.get("PATH", ''),
            QUERY_STRING=request.META.get("QUERY_STRING", ''),
            REMOTE_ADDR=request.META.get("REMOTE_ADDR", ''),
            REMOTE_HOST=request.META.get("REMOTE_HOST", ''),
            REMOTE_USER=request.META.get("SCRIPT_NAME", ''),
            REQUEST_METHOD=request.META.get("REQUEST_METHOD", ''),
            encoding=request.encoding,
            SERVER_PORT=request.META.get("SERVER_PORT", ''),
            GET=request.GET,
            COOKIES=request.META.get("CSRF_COOKIE", ''),

            # json.loads(request.GET.dict().keys()[0])
            # json.dumps({k: request.GET.getlist(k) for k in request.GET.keys()})
        )

        # sprint(data_json)
        # RequestHederInfo.objects.create(
        #     datajson=json.loads(request.META))
        # from django.core import serializers
        # import json
        # ip = request.META.get('REMOTE_ADDR')

        my_dict = {
            # 'body': request,
            'fromUrl': fromUrl,
            'headers': {k.lower(): v for (k, v) in request.headers.items()}
        }
        # tmpJson = serializers.serialize("json",request.headers)
        # tmpObj = json.loads(tmpJson)
        # print(request.headers)
        RequestHederInfo.objects.create(datajson=my_dict,
                                        cookie=cookie,
                                        ip_info=ip_info,

                                        )
    except ValueError as e:
        print("ValueError "+str(e))
    except requests.exceptions.ConnectionError as e:
        print("requests exceptions ConnectionError "+str(e))
    except Exception as e:
        print("requests exception  "+str(e))
    # except request.exceptions.ConnectionError:
        # pass


class SaveInfoIpMiddleware(MiddlewareMixin):
    header = "Save_Info"
    force_logout_if_no_header = True
    def process_request(self, request):
        import random
        import string
        rend = HttpResponse(request, 'index.html')
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(100))
        req = request
        set_cookie_page(req, rend, getUrl(request=request))
        print(type(self))
        print(type(request))
        try:
            print("sessionid : " + str(request.session.get('sessionid')))

            print("session get : " + str(request.session.get))


        except KeyError as e:
            print("KeyError" + str(e))

        try:
            username = request.META[self.header]
        except KeyError as e:
            # If specified header doesn't exist then remove any existing
            # authenticated remote-user, or return (leaving request.user set to
            # AnonymousUser by the AuthenticationMiddleware).
            # if self.force_logout_if_no_header and request.user.is_authenticated:
            # return
            print("KeyError" + str(e))

        print("request:" + str(request))


        saveInfoIp(request, getUrl(request=request))

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        # if not hasattr(request, "session"):
            # raise ImproperlyConfigured(
            #     "The Django authentication middleware requires session "
            #     "middleware to be installed. Edit your MIDDLEWARE setting to "
            #     "insert "
            #     "'django.contrib.sessions.middleware.SessionMiddleware' before "
            #     "'django.contrib.auth.middleware.AuthenticationMiddleware'."
            # )
        request.user = SimpleLazyObject(lambda: get_user_admin(request))


class RemoteUserMiddleware(MiddlewareMixin):
    """
    Middleware for utilizing web-server-provided authentication.

    If request.user is not authenticated, then this middleware attempts to
    authenticate the username passed in the ``REMOTE_USER`` request header.
    If authentication is successful, the user is automatically logged in to
    persist the user in the session.

    The header used is configurable and defaults to ``REMOTE_USER``.  Subclass
    this class and change the ``header`` attribute if you need to use a
    different header.
    """

    # Name of request header to grab username from.  This will be the key as
    # used in the request.META dictionary, i.e. the normalization of headers to
    # all uppercase and the addition of "HTTP_" prefix apply.
    header = "REMOTE_USER"
    force_logout_if_no_header = True

    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, "user"):
            raise ImproperlyConfigured(
                "The Django remote user auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the RemoteUserMiddleware class."
            )
        try:
            username = request.META[self.header]
        except KeyError:
            # If specified header doesn't exist then remove any existing
            # authenticated remote-user, or return (leaving request.user set to
            # AnonymousUser by the AuthenticationMiddleware).
            if self.force_logout_if_no_header and request.user.is_authenticated:
                self._remove_invalid_user(request)
            return
        # If the user is already authenticated and that user is the user we are
        # getting passed in the headers, then the correct user is already
        # persisted in the session and we don't need to continue.
        if request.user.is_authenticated:
            if request.user.get_username() == self.clean_username(username, request):
                return
            else:
                # An authenticated user is associated with the request, but
                # it does not match the authorized user in the header.
                self._remove_invalid_user(request)

        # We are seeing this user for the first time in this session, attempt
        # to authenticate the user.
        user = auth.authenticate(request, remote_user=username)
        if user:
            # User is valid.  Set request.user and persist user in the session
            # by logging the user in.
            request.user = user
            auth.login(request, user)

    def clean_username(self, username, request):
        """
        Allow the backend to clean the username, if the backend defines a
        clean_username method.
        """
        backend_str = request.session[auth.BACKEND_SESSION_KEY]
        backend = auth.load_backend(backend_str)
        try:
            username = backend.clean_username(username)
        except AttributeError:  # Backend has no clean_username method.
            pass
        return username

    def _remove_invalid_user(self, request):
        """
        Remove the current authenticated user in the request which is invalid
        but only if the user is authenticated via the RemoteUserBackend.
        """
        try:
            stored_backend = load_backend(
                request.session.get(auth.BACKEND_SESSION_KEY, "")
            )
        except ImportError:
            # backend failed to load
            auth.logout(request)
        else:
            if isinstance(stored_backend, RemoteUserBackend):
                auth.logout(request)


class PersistentRemoteUserMiddleware(RemoteUserMiddleware):
    """
    Middleware for web-server provided authentication on logon pages.

    Like RemoteUserMiddleware but keeps the user authenticated even if
    the header (``REMOTE_USER``) is not found in the request. Useful
    for setups when the external authentication via ``REMOTE_USER``
    is only expected to happen on some "logon" URL and the rest of
    the application wants to use Django's authentication mechanism.
    """

    force_logout_if_no_header = False
