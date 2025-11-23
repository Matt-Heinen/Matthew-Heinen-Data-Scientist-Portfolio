// Navigation
function TopNav() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
function SecNav() {
    var x = document.getElementById("mySecnav");
    if (x.className === "secnav") {
        x.className += " responsive";
    } else {
        x.className = "secnav";
    }
}

// Search Typeahead
$(document).ready(function(){
    $('#ballpark_search .typeahead').typeahead({
            name: 'typeahead',
            remote:'/ballparks/includes/search_code.php?key=%QUERY',
            limit : 10
    });
});


// Tooltip https://osvaldas.info/elegant-css-and-jquery-tooltip-responsive-mobile-friendly
$( function(){
    var targets = $( '[rel~=tooltip]' ),
        target  = false,
        tooltip = false,
        title   = false;
 
    targets.bind( 'mouseenter', function(){
        target  = $( this );
        tip     = target.attr( 'title' );
        tooltip = $( '<div id="tooltip"></div>' );
 
        if( !tip || tip == '' )
            return false;
 
        target.removeAttr( 'title' );
        tooltip.css( 'opacity', 0 )
               .html( tip )
               .appendTo( 'body' );
 
        var init_tooltip = function(){
            if( $( window ).width() < tooltip.outerWidth() * 1.5 )
                tooltip.css( 'max-width', $( window ).width() / 2 );
            else
                tooltip.css( 'max-width', 340 );
 
            var pos_left = target.offset().left + ( target.outerWidth() / 2 ) - ( tooltip.outerWidth() / 2 ),
                pos_top  = target.offset().top - tooltip.outerHeight() - 20;
 
            if( pos_left < 0 )
            {
                pos_left = target.offset().left + target.outerWidth() / 2 - 20;
                tooltip.addClass( 'left' );
            }
            else
                tooltip.removeClass( 'left' );
 
            if( pos_left + tooltip.outerWidth() > $( window ).width() )
            {
                pos_left = target.offset().left - tooltip.outerWidth() + target.outerWidth() / 2 + 20;
                tooltip.addClass( 'right' );
            }
            else
                tooltip.removeClass( 'right' );
 
            if( pos_top < 0 )
            {
                var pos_top  = target.offset().top + target.outerHeight();
                tooltip.addClass( 'top' );
            }
            else
                tooltip.removeClass( 'top' );
 
            tooltip.css( { left: pos_left, top: pos_top } )
                   .animate( { top: '+=10', opacity: 1 }, 50 );
        };
 
        init_tooltip();
        $( window ).resize( init_tooltip );
 
        var remove_tooltip = function()
        {
            tooltip.animate( { top: '-=10', opacity: 0 }, 50, function()
            {
                $( this ).remove();
            });
 
            target.attr( 'title', tip );
        };
 
        target.bind( 'mouseleave', remove_tooltip );
        tooltip.bind( 'click', remove_tooltip );
    });
});
  

// Table clone for scrolling on smaller screens
$(function(){
        var $table = $('.main_table');
        //Make a clone of our table
        var $fixedColumn = $table.clone().insertBefore($table).addClass('fixed-column');

        //Remove everything except for first column
        $fixedColumn.find('th:not(:nth-child(1)),td:not(:nth-child(1))').remove();

        //Match the height of the rows to that of the original table's
        $fixedColumn.find('tr').each(function (i, elem) {
            $(this).height($table.find('tr:eq(' + i + ')').height());
        });
        });