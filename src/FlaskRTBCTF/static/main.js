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
    $('#m-rate').on('show.bs.modal', function (event) {
	const button = $(event.relatedTarget);
        const boxId = button.data('boxid'); // Extract info from data-* attributes
        $(this).find('#machine-id-rating').val(boxId);
    })

    //challenge rating submission modal
    $('#c-rate').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const challengeId = button.data('chid'); // Extract info from data-* attributes
        $(this).find('#machine-id-rating').val(challengeId);
    })

});
