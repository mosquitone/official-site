
$(window)
  .on('load', function () {
    $('main .official.header.container').transition(
      {
        animation: 'fade',
        duration: '1s',
        onComplete: function () {
          $('main .ui.sub.header').transition({
            animation: 'fade',
            duration: '0.6s',
            onComplete: function () {
              $('main .ui.primary.button').transition({
                animation: 'fade',
                duration: '0.3s',
                onComplete: function () {
                  $('main .ui.secondary.button').transition({
                    animation: 'fade',
                    duration: '0.3s',
                  });
                }
              }
              )
            }
          }
          )
        }
      }
    );
  }
  )
