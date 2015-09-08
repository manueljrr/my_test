__author__ = 'Manuel'

import xlsxwriter
from xlsxwriter.utility import xl_range_abs
from django.views.generic import View, TemplateView, CreateView, ListView
from django.http import HttpResponse, HttpResponseNotFound

from .models import Producto
from .forms import ProductoForm

class ExcelExport(View):
    filename = 'excelfile.xlsx'

    def get(self, request, *args, **kwargs):
        # Get data - here data list example
        data = list()
        data.append(('Apple', 25))
        data.append(('Peach', 28))
        data.append(('Orange', 17))

        # Create and open the file
        wb = xlsxwriter.Workbook(self.filename)

        # Add Worksheet
        sheet = wb.add_worksheet('sheet1')

        # Set formats
        section_header_format = wb.add_format({
            'bold': True,
            'align': 'left',
            'font_size': 16,
        })

        # define num format
        num_format = wb.add_format({
            'num_format': '0',
            'align': 'right',
            'font_size': 12,
        })

        # define general format
        general_format = wb.add_format({
            'align': 'left',
            'font_size': 12,
        })

        # Define cols Width
        sheet.set_column(0, 0, 45, general_format)
        sheet.set_column(1, 1, 20, num_format)


        # Insert a header image.
        sheet.insert_image(1, 0, 'logo.jpeg')

        # Write and merge cells
        sheet.merge_range(6, 0, 6, 1, 'El WebMaster Sample', section_header_format)


        row = 8
        sheet.write(row, 0, 'Fruta')
        sheet.write(row, 1, 'Cantidad')

        for obj in data:
            row += 1
            sheet.write_row(row, 0, obj)

        # Close file
        wb.close()

        # Response
        return HttpResponse(open(self.filename, 'r').read(), content_type='application/ms-excel')


class CreateProductView(CreateView):
    form_class = ProductoForm
    template_name = 'my_table.html'


class TagFilterView(TemplateView):
    template_name = 'tag_filter.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return super(TagFilterView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TagFilterView, self).get_context_data(**kwargs)

        context['monto'] = 563.43565243
        return context


class AdjusterView(TemplateView):
    template_name = 'date_adjuster.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return super(AdjusterView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdjusterView, self).get_context_data(**kwargs)

        import datetime
        context['mi_fecha'] = datetime.datetime.now()
        context['name'] = 'Manuel'
        return context

class TableView(TemplateView):
    template_name = 'my_table.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = ProductoForm()
        if not context:
            raise Exception('Context not set in view')

        return super(TableView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            print 'yes done'
            #save your model
            #redirect

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)

        context['form'] = ProductoForm()
        context['name'] = 'Manuel'
        context['surname'] = 'Rosa'
        context['city'] = 'Madrid'
        context['country'] = 'Spain'
        context['zipcode'] = '28027'
        return context


def home(name):
    return HttpResponse('Holaaaa')


class ExcelExportTable(View):
    filename = 'excelfile.xlsx'

    def get(self, request, *args, **kwargs):
        # Get data - here data list example
        data = list()
        data.append(('Apple', 25))
        data.append(('Peach', 28))
        data.append(('Orange', 17))

        # Create and open the file
        wb = xlsxwriter.Workbook(self.filename)

        # Add Worksheet
        sheet = wb.add_worksheet('sheet1')

        # Set formats
        section_header_format = wb.add_format({
            'bold': True,
            'align': 'left',
            'font_size': 16,
        })

        #define num format
        num_format = wb.add_format({
            'num_format': '0',
            'align': 'right',
            'font_size': 12,
        })

        #define general format
        general_format = wb.add_format({
            'align': 'left',
            'font_size': 12,
        })

        # Define cols Width
        sheet.set_column(0, 0, 45)
        sheet.set_column(1, 1, 20)

        # Insert a header image.
        sheet.insert_image(1, 0, 'logo.jpeg')

        # Write and merge cells
        sheet.merge_range(6, 0, 6, 1, 'El WebMaster - Excel Sample', section_header_format)

        options = {
            'data': data,
            'total_row': data.__len__(),
            'banded_rows': False,
            'style': 'Table Style Light 9',
            'columns': [
                {'header': 'Fruit', 'total_string': 'Total', 'format': general_format},
                {'header': 'Count', 'total_function': 'sum', 'format': num_format}
            ]
        }

        start_row = 9
        end_row = start_row + data.__len__() + 1
        sheet.add_table(start_row, 0, end_row, 1, options)

        # Create a chart
        chart = wb.add_chart({'type': 'pie'})
        # Set chart title
        chart.title_name = 'Fruits piechart'
        # Set width fixed to cols
        chart.width = sheet._size_col(0) + sheet._size_col(1)

        # Set value range  i.e. =sheet1!$B$11:$B$13
        values = '=%s!%s' % (sheet.name, xl_range_abs(start_row+1, 1, end_row-1, 1))
        # Set category range  i.e. =sheet1!$A$11:$A$13
        categories = '=%s!%s' % (sheet.name, xl_range_abs(start_row+1, 0, end_row-1, 0))
        # Add series to chart
        chart.add_series({'values': values, 'categories': categories, 'smooth': True})

        # Insert chart into the sheet
        sheet.insert_chart(end_row + 2, 0, chart)

        # Close file
        wb.close()

        # Response
        return HttpResponse(open(self.filename, 'r').read(),
                            content_type='application/ms-excel')


class ExcelExportChart(View):
    filename = 'excelfile.xlsx'

    def get(self, request, *args, **kwargs):
        # Get data - here data list example
        data = list()
        data.append(('Apple', 25))
        data.append(('Peach', 28))
        data.append(('Orange', 17))

        # Create and open the file
        wb = xlsxwriter.Workbook(self.filename)

        # Add Worksheet
        sheet = wb.add_worksheet('sheet1')

        # Set formats
        section_header_format = wb.add_format({
            'bold': True,
            'align': 'left',
            'font_size': 16,
        })

        #define num format
        num_format = wb.add_format({
            'num_format': '0',
            'align': 'right',
            'font_size': 12,
        })

        #define general format
        general_format = wb.add_format({
            'align': 'left',
            'font_size': 12,
        })

        # Define cols Width
        sheet.set_column(0, 0, 45)
        sheet.set_column(1, 1, 20)


        # Insert a header image.
        sheet.insert_image(1, 0, 'logo.jpeg')

        # Write and merge cells
        sheet.merge_range(6, 0, 6, 1, 'El WebMaster - Excel Sample', section_header_format)

        options = {
            'data': data,
            'total_row': data.__len__(),
            'banded_rows': False,
            'style': 'Table Style Light 9',
            'columns': [
                {'header': 'Fruit', 'total_string': 'Total', 'format': general_format},
                {'header': 'Count', 'total_function': 'sum', 'format': num_format}
            ]
        }

        start_row = 9
        end_row = start_row + data.__len__() + 1
        sheet.add_table(start_row, 0, end_row, 1, options)

        # Create a chart
        chart = wb.add_chart({'type': 'pie'})
        # Set chart title
        chart.title_name = 'Fruits piechart'
        # Set width fixed to cols
        chart.width = sheet._size_col(0) + sheet._size_col(1)

        # Set value range  i.e. =sheet1!$B$11:$B$13
        values = '=%s!%s' % (sheet.name, xl_range_abs(start_row+1, 1, end_row-1, 1))
        # Set category range  i.e. =sheet1!$A$11:$A$13
        categories = '=%s!%s' % (sheet.name, xl_range_abs(start_row+1, 0, end_row-1, 0))
        # Add series to chart
        chart.add_series({'values': values, 'categories': categories, 'smooth': True})

        # Insert chart into the sheet
        sheet.insert_chart(end_row + 2, 0, chart)

        # Close file
        wb.close()

        # Response
        return HttpResponse(open(self.filename, 'r').read(), content_type='application/ms-excel')


