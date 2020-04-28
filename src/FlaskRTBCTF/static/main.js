$(document).ready( function() {

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip(
        {
        'delay': { show: 50, hide: 50 }
        }
    );

    // modal
    $('#m-form').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const boxId = button.data('boxid'); // Extract info from data-* attributes
        var modal = $(this);
        modal.find('#machine-id-user').val(boxId);
        modal.find('#machine-id-root').val(boxId);
    })
});