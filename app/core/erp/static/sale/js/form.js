var tblProducts;
var vents = {
    items : {
        cli: '',
        date_joinder: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        products: []
    },
    calculate_invoice: function(){
        var subtotal = 0.00;
        var iva =  $('input[name="iva"]').val()
        $.each(this.items.products, function(pos, dict){
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal+=dict.subtotal;
            
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.iva + subtotal
        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacal"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    
    add: function(item){
        this.items.products.push(item);
        this.list();
    },

    list: function () {
        this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            data: this.items.products,
            rowCallback( row, data, displayNum, displayIndex, dataIndex ){
                // row nos devuelve el tr, y luego bucamos el elemento
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });                                
            },
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "cat.name"},
                {"data": "pvp"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' +parseFloat(data).toFixed(2);
                        
                    }
                }, 
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class"form-control form-control-sm input-sm" autocomplete="off" value="'+data+'" >';
                        
                    }
                },  
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' +parseFloat(data).toFixed(2);
                        
                    }
                },                                              
            ],
            initComplete: function (settings, json) {
    
            }
        });        

    }
}

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function (){
        vents.calculate_invoice();
    })
    .val(0.19);

    // Buscqueda de productos

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            // console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0;
            vents.add(ui.item);
            // console.log(vents.items)
            $(this).val('');
        }
    });    

    $('#tblProducts tbody').on('change', 'input[name="cant"]', function(){
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        vents.items.products[tr.row].cant = cant;
        vents.calculate_invoice();
        $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' +  vents.items.products[tr.row].subtotal.toFixed(2));

    });
});