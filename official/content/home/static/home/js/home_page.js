
$(window)
  .on('load', function () {
    $('main .official.header.container').transition(
      {
        animation: 'fade',
        duration: '1.5s',
        onComplete: function () {
          $('main .ui.sub.header').transition({
            animation: 'fade',
            duration: '0.6s',
            onComplete: $('main .official.link.buttons > .button').toArray().reverse().reduce(function (nextButtonTransition, currentButton) {
              var transitionParameter = {
                animation: 'fade',
                duration: '0.3s',
              }
              if (nextButtonTransition) {
                transitionParameter.onComplete = nextButtonTransition;
              }
              return function () {
                $(currentButton).transition(transitionParameter)
              }
            }, null)
          }
          )
        }
      }
    );
  }
  )
