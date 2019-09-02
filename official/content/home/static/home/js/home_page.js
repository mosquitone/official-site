
$(window)
  .on('load', function () {
    $('.masthead .official.header.container').transition(
      {
        animation: 'fade',
        duration: '1s',
        onComplete: function () {
          $('.masthead .ui.sub.header').transition({
            animation: 'fade',
            duration: '0.6s',
            onComplete: function () {
              $('.masthead .ui.primary.button').transition({
                animation: 'fade',
                duration: '0.3s',
                onComplete: function () {
                  $('.masthead .ui.secondary.button').transition({
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
