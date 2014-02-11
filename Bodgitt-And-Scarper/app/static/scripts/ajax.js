/**
 * AJAX: Some simple, handy scripts for asynchronous communications.
 *
 * Version: 0.1
 *
 * License: Public Domain
 *
 * Author: Robert Harder
 *         rharder@users.sf.net
 *
 * Functions for you to call:
 *
 *     AJAX.getXML( url, callback )
 *         Retrieves 'url' and attempts to parse as XML.
 *         The xml DOM object is passed to the 'callback'
 *         function which should accept a single argument,
 *         the xml DOM object.
 *
 *     AJAX.getText( url, callback )
 *         Retrieves 'url' and passes the raw returned text
 *         to the 'callback' function which should accept a
 *         single argument, the text string.
 *
 *     AJAX.setValue( url, element )
 *         Retrieves raw text from 'url' and attempts to set
 *         the 'value' property of 'element'.
 *
 *     AJAX.setValueById( url, id )
 *         Retrieves raw text from 'url' and attempts to set
 *         the 'value' property of element 'id'.
 *
 *     AJAX.setInnerHTML( url, element )
 *         Retrieves raw text from 'url' and attempts to set
 *         the 'innerHTML' property of 'element'.
 *
 *     AJAX.setInnerHTMLById( url, id )
 *         Retrieves raw text from 'url' and attempts to set
 *         the 'innerHTML' property of element 'id'.
 *
 *
 * Condensed Example:
 *
 *     <p>
 *       The answer to Life, the Universe, and Everything:
 *       <span id="answer">Waiting for Deep Thought...</span>
 *     </p>
 *     <script src="ajax.js" type="text/javascript" ></script>
 *     <script>
 *       AJAX.setInnerHTMLById( 'deepthought.php?action=thinkhard', answer )
 *     </script>
 *
 */


////
// If AJAX is not yet defined, define it.
// This protects against AJAX accidentally
// being included more than once.
////
//if( typeof AJAX == 'undefined' ){

AJAX = {


    /**
     * Retrieves 'url' and attempts to parse as XML.
     * The xml DOM object is passed to the 'callback'
     * function which should accept a single argument,
     * the xml DOM object.
     */
    getXML : function( url, callback )
    {
        return AJAX.ajaxFull( url, callback, false );
    },  // end getXML



    /**
     * Retrieves 'url' and passes the raw returned text
     * to the 'callback' function which should accept a
     * single argument, the text string.
     */
    getText : function( url, callback )
    {
        return AJAX.ajaxFull( url, callback, true );
    },  // end getText



    /**
     * Retrieves raw text from 'url' and attempts to set
     * the 'innerHTML' property of 'element'.
     */
    setInnerHTML: function ( url, element )
    {
        AJAX.getText( url, function( text ){

            if( element && element.innerHTML )
                element.innerHTML = text;

        }); // end ajax function
    },  // end setInnerHTML



    /**
     * Retrieves raw text from 'url' and attempts to set
     * the 'innerHTML' property of element 'id'.
     */
    setInnerHTMLById : function( url, id )
    {
        if( document.getElementById )
            return AJAX.setInnerHTML( url, document.getElementById( id ) );

    },  // end setInnerHTMLById



    /**
     * Retrieves raw text from 'url' and attempts to set
     * the 'value' property of 'element'.
     */
    setValue: function ( url, element )
    {
        AJAX.getText( url, function( text ){

            if( element && element.value )
                element.value = text;

        }); // end ajax function
    },  // end setInnerHTML


    /**
     * Retrieves raw text from 'url' and attempts to set
     * the 'value' property of element 'id'.
     */
    setValueById : function( url, id )
    {
        if( document.getElementById )
            return AJAX.setValue( url, document.getElementById( id ) );

    },  // end setValueById


/* ********  I N T E R N A L   F U N C T I O N S  ******** */


    ////
    // Used internally to retrieve text asynchronously.
    ////
    ajaxFull : function( url, callback, textInsteadOfXml )
    {
        var request = AJAX.httprequest();
        request.open("GET", url, true);
        request.onreadystatechange = function() {
            if( request.readyState == 4 ) {

                // Text
                if( textInsteadOfXml ) {

                    callback( request.responseText );

                } // end if: text

                // XML
                else {

                    var xmlDoc = request.responseXML;

                    // Special case: if we're using Google's stuff
                    // use their parser as a fallback.
                    if( xmlDoc.documentElement == null && GXml && GXml.parse )
                        xmlDoc = GXml.parse( request.responseText );

                    callback( xmlDoc );

                } // end else: xml
            } // end if: ready state 4
        }; // end on ready state change

        request.send(null);

    },// end ajax


    ////
    // Used internally to create HttpRequest.
    ////
    httprequest : function()
    {
        // Microsoft?
        if( typeof ActiveXObject != 'undefined' ){
            try {
                return new ActiveXObject( 'Microsoft.XMLHTTP' );
            } catch( exc ) {
                // error
            }   // end catch: exception
        }   // end if: Microsoft

        // Standard?
        if( typeof XMLHttpRequest != 'undefined' ){
            try {
                return new XMLHttpRequest();
            } catch( exc ) {
                // error
            }   // end catch: exception
        }   // end if: Standard
    }

}   // end AJAX


//}   // end if: AJAX not already defined

