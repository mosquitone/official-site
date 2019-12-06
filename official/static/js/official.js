$(document)
  .ready(function () {
    // change wagtail richtext to semantic ui container
    $('div.rich-text').each(function (_, e) {
      e.classList.remove('rich-text');
      e.classList.add('ui', 'container');
    })
    // change wagtail image in richtext to semantic ui image
    $('img.richtext-image').each(function (_, e) {
      e.classList.remove('richtext-image');
      e.classList.add('ui', 'image');
      e.style.width = "auto";
      e.style.height = "auto";
    })

    // fix menu when passed
    $('.masthead')
      .visibility({
        once: false,
        onBottomPassed: function () {
          $('.fixed.menu').transition('fade down');
        },
        onBottomPassedReverse: function () {
          $('.fixed.menu').transition('fade down');
        }
      })
      ;
    // create sidebar and attach to menu open
    $('.ui.sidebar')
      .sidebar('attach events', '.toc.item')
      ;
    // activate menu link
    var topLevelPath = '/' + window.location.pathname.split('/')[1];
    if (!topLevelPath.endsWith('/')) {
      topLevelPath += '/';
    }
    $('.link.menu > a.item').each(function () {
      if (!this.href) {
        return;
      }
      if (topLevelPath == new URL(this.href).pathname) {
        $(this).addClass('active');
      }
    });

    // set <a> tag has link other domain to target=_blank
    $('a[href^="http://"],a[href^="https://"]').not('a[href^="' + location.origin + '"]')
      .attr('target', '_blank')
      .attr('rel', 'noopener noreferrer');

    // initialize accordion
    $('.ui.accordion').accordion();

    // initialize mosquitone share
    if (navigator.share) {
      $('.official.share').each((_, e) => {
        e.classList.add('enable');
        e.addEventListener('click', async () => {
          const shareData = {
            title: document.title,
            url: '',
            ...e.dataset
          }
          if (!shareData.url && 'text' in shareData) {
            // Append current page url to end of text
            const currentUrl = location.protocol + '//' + location.host + location.pathname;
            shareData.text = shareData.text + '\n' + currentUrl;
          }
          try {
            await navigator.share(shareData);
          } catch (err) {
            // noop
          }
        });
      });
    }
  })
  ;
