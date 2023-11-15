# from django.db.models import Sum, Count
# from django.utils.translation import gettext_lazy as _
# from slick_reporting.generator import Chart

# from erp_framework.reporting.registry import register_report_view
# from erp_framework.reporting.views import ReportView
# from slick_reporting.fields import SlickReportField, TotalReportField
# from slick_reporting.views import SlickReportView
# from .models import Country, Region


# @register_report_view
# class TotalCountry(ReportView):
#     # the model to use for the report
#     report_model = Region
#     date_field = "edit_at"
#     report_title = "Total Country"
#     group_by = "country"
#     columns = ["name", SlickReportField.create(
#         Count, "country", name='price__sum', verbose_name="Total Count"),]

#     # columns = [
#     #     "name",
#     #     # SlickReportField.create(Count, "country__id"),
#     #     SlickReportField.create(Count, "country", name="sum__country"),
#     #      SlickReportField.create(
#     #         Sum, "country", verbose_name=_("Sales region"), name="country"
#     #     )
#     # ]
#     # columns = [
#     # "name",
#     # SlickReportField.create(Count, "id", verbose_name="Total Count"),
#     # ]

#     # default_order_by = "-count__id"

#     chart_settings = [
#         Chart(
#             "name",
#             Chart.COLUMN,
#             title_source=["name"],
#             data_source=["price__sum"],
#             plot_total=True,
#         ),
#     ]
#     # time_series_pattern = (
#     #     "monthly"  # or "yearly" , "weekly" , "daily" , others and custom patterns
#     # )

#     # chart_settings = [
#     #     Chart(
#     #         "Total sold $",
#     #         Chart.LINE,
#     #         data_source="sum__country",
#     #         title_source="title",
#     #     ),
#     # ]


# class TotalRegon(SlickReportField):
#     calculation_method = Count
#     calculation_field = "country_id"
#     is_summable = True
#     verbose_name = _("Count region")
#     name = "total_regon"


# class PercentageToTotalRegon(SlickReportField):
#     requires = (TotalRegon,)
#     # prevent_group_by = True
#     # is_summable = False
#     calculation_field = "country_id"
#     name = "percentage"
#     verbose_name = _("% Count")

#     @classmethod
#     def get_time_series_field_verbose_name(cls, date_period, index, dates, pattern):
#         return "%"

#     def final_calculation(self, debit, credit, dep_dict):
#         debit = debit or 0
#         credit = credit or 0
#         try:
#             return round((dep_dict.get("total_regon", 0) / (debit - credit)) * 100, 2)
#         except ZeroDivisionError:
#             return 0


# @register_report_view
# class TotalRegionTimeSeriesWithPercentage(ReportView):
#     report_model = Region
#     # base_model = Product

#     # the field to use for the date
#     # date_field = "date"
#     date_field = "edit_at"
#     report_title = "Total Count Country"
#     group_by = "country"
#     # report_title = "Product Sales Time Series (with %)"

#     # the field to use for the group by
#     # group_by = "product"

#     # Columns to display ,
#     columns = [
#         "name",
#         "__time_series__",
#         TotalRegon,
#         PercentageToTotalRegon,
#     ]

#     time_series_selector = True
#     time_series_selector_default = "monthly"
#     #
#     time_series_columns = [
#         TotalRegon,
#         PercentageToTotalRegon,
#     ]

#     chart_settings = [
#         {
#             "type": "column",
#             "data_source": ["total_regon"],
#             "title_source": ["name"],
#         },
#         {
#             "title": "Total",
#             # "engine_name": "chartsjs",
#             "type": "column",
#             "data_source": ["total_regon"],
#             "title_source": ["name"],
#             "plot_total": True,
#         },
#         {
#             "title": "Total",
#             # "engine_name": "chartsjs",
#             "type": "pie",
#             "data_source": ["total_regon"],
#             "title_source": ["name"],
#             "plot_total": True,
#         },
#     ]


# @register_report_view
# class TotalCountrysss(ReportView):
#     # the model to use for the report
#     report_model = Country
#     date_field = "edit_at"
#     report_title = "Total Countrysss"
#     group_by = "name"
#     columns = ["id", SlickReportField.create(
#         Sum, "code2", name='price__sum', verbose_name="Total Count"),]

#     # columns = [
#     #     "name",
#     #     # SlickReportField.create(Count, "country__id"),
#     #     SlickReportField.create(Count, "country", name="sum__country"),
#     #      SlickReportField.create(
#     #         Sum, "country", verbose_name=_("Sales region"), name="country"
#     #     )
#     # ]
#     # columns = [
#     # "name",
#     # SlickReportField.create(Count, "id", verbose_name="Total Count"),
#     # ]

#     # default_order_by = "-count__id"

#     chart_settings = [
#         Chart(
#             "id",
#             Chart.PIE,
#             title_source=["name"],
#             data_source=["price__sum"],
#             plot_total=True,
#         ),
#     ]
#     # time_series_pattern = (
#     #     "monthly"  # or "yearly" , "weekly" , "daily" , others and custom patterns
#     # )

#     # chart_settings = [
#     #     Chart(
#     #         "Total sold $",
#     #         Chart.LINE,
#     #         data_source="sum__country",
#     #         title_source="title",
#     #     ),
#     # ]


# @register_report_view
# class CrossTabReportView(ReportView):
#     report_title = "Cross Tab ReportView"
#     report_model = Region
#     date_field = 'edit_at'
#     group_by = 'country'
#     columns = ['id', SlickReportField.create(
#         Sum, 'country', name='region__sum', verbose_name=_('Sales'))]

#     # To activate Crosstab
#     # crosstab_model = 'Country'
#     # we corsstab on a foreignkey field

#     chart_settings = [
#         Chart(
#             "Total sold $",
#             Chart.LINE,
#             data_source="id",
#             # data_source="region__sum",
#             title_source="id",

#         ),
#     ]
