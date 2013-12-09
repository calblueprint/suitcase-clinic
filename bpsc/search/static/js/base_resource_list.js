$(document).ready(function()
    {
        $("#resource-table").tablesorter();
    }

    function getParameter(paramName) {
      var searchString = window.location.search.substring(1),
          i, val, params = searchString.split("&");
      for (i=0;i<params.length;i++) {
        val = params[i].split("=");
        if (val[0] == paramName) {
          return unescape(val[1]);
        }
      }
      return null;
    }

    $(window).load(function(){
        if (getParamater('form_error') === 'true') {
            $('#printModal').modal('show');
        }
    });

);
