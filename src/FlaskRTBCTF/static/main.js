$(document).ready( function() {

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip(
        {
        'delay': { show: 50, hide: 50 }
        }
    );

    // machine user hash submission modal
    $('#m-form-user').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const boxId = button.data('boxid'); // Extract info from data-* attributes
        var modal = $(this);
        modal.find('#machine-id-user').val(boxId);
    })

    // machine root hash submission modal
    $('#m-form-root').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const boxId = button.data('boxid'); // Extract info from data-* attributes
        var modal = $(this);
        modal.find('#machine-id-root').val(boxId);
    })

    // challenge flag submission
    $('#c-form').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const challengeId = button.data('chid'); // Extract info from data-* attributes
        $(this).find('#challenge-id').val(challengeId);
    })

    // machine rating submission modal
    $('#m-form-rate').on('show.bs.modal', function (event) {
	    const button = $(event.relatedTarget);
        const boxId = button.data('boxid'); // Extract info from data-* attributes
        $(this).find('#rating-id').val(boxId);
        $(this).find('#rating-for').val('machine');
    })

    //challenge rating submission modal
    $('#c-form-rate').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const challengeId = button.data('chid'); // Extract info from data-* attributes
        $(this).find('#rating-id').val(challengeId);
        $(this).find('#rating-for').val('challenge');
    })

});
