/**
 * FASHION VILLAGE - HERITAGE WEAVES & SILKS
 * Core Application Interactions & Dynamic Experience
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Currency Conversion & Exchange Rates
  // -------------------------------------------------------------------------
  const currencyRates = {
    INR: { symbol: '₹', rate: 1, format: (val) => `₹${val.toLocaleString('en-IN')}` },
    USD: { symbol: '$', rate: 0.012, format: (val) => `$${Math.round(val * 0.012).toLocaleString()}` },
    EUR: { symbol: '€', rate: 0.011, format: (val) => `€${Math.round(val * 0.011).toLocaleString()}` },
    GBP: { symbol: '£', rate: 0.0095, format: (val) => `£${Math.round(val * 0.0095).toLocaleString()}` },
    AED: { symbol: 'AED ', rate: 0.044, format: (val) => `AED ${Math.round(val * 0.044).toLocaleString()}` }
  };

  let currentCurrency = 'INR';

  function updatePrices(currencyCode) {
    currentCurrency = currencyCode;
    const config = currencyRates[currencyCode] || currencyRates.INR;

    document.querySelectorAll('[data-inr-price]').forEach(el => {
      const inrValue = parseFloat(el.getAttribute('data-inr-price'));
      el.textContent = config.format(inrValue);
    });

    const selectorLabel = document.getElementById('current-currency-label');
    if (selectorLabel) {
      selectorLabel.textContent = `${config.symbol} ${currencyCode} (${config.symbol.trim()})`;
    }

    showToast(`Currency updated to ${currencyCode}`);
  }

  // -------------------------------------------------------------------------
  // 2. Announcement Bar Carousel / Ticker
  // -------------------------------------------------------------------------
  const announcements = [
    'COMPLIMENTARY WORLDWIDE SHIPPING ON PURE SILK SAREES ABOVE ₹5,000 • FESTIVE CONNOISSEUR COLLECTION LIVE',
    'HANDLOOM CERTIFIED • 100% PURITY TESTED SILVER-GILT METALLIC ZARI • 45 YEARS OF MASTER CRAFTSMANSHIP',
    'NOW OPEN: BESPOKE BRIDAL SUITE IN CHENNAI & BENGALURU • BOOK PRIVATE VIDEO CONSULTATIONS'
  ];

  let currentAnnouncementIndex = 0;
  const announcementEl = document.getElementById('announcement-text');
  const prevBtn = document.getElementById('announcement-prev');
  const nextBtn = document.getElementById('announcement-next');

  function renderAnnouncement(index) {
    if (!announcementEl) return;
    announcementEl.style.opacity = '0';
    setTimeout(() => {
      announcementEl.textContent = announcements[index];
      announcementEl.style.opacity = '1';
    }, 200);
  }

  if (announcementEl) {
    renderAnnouncement(0);
    setInterval(() => {
      currentAnnouncementIndex = (currentAnnouncementIndex + 1) % announcements.length;
      renderAnnouncement(currentAnnouncementIndex);
    }, 5500);

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        currentAnnouncementIndex = (currentAnnouncementIndex - 1 + announcements.length) % announcements.length;
        renderAnnouncement(currentAnnouncementIndex);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        currentAnnouncementIndex = (currentAnnouncementIndex + 1) % announcements.length;
        renderAnnouncement(currentAnnouncementIndex);
      });
    }
  }

  // -------------------------------------------------------------------------
  // 3. Search Autocomplete & Focus Interactions
  // -------------------------------------------------------------------------
  const searchInput = document.getElementById('search-input');
  const searchDropdown = document.getElementById('search-dropdown');

  if (searchInput && searchDropdown) {
    searchInput.addEventListener('focus', () => {
      searchDropdown.classList.add('active');
    });

    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      const resultsContainer = document.getElementById('search-live-results');
      if (resultsContainer) {
        if (query.length > 1) {
          resultsContainer.innerHTML = `
            <div class="dropdown-item" onclick="triggerSearch('${query} in Kanchipuram')">
              <span><strong>${e.target.value}</strong> in Pure Kanchipuram</span>
              <span style="font-size:11px;color:#8C6E18;">42 Weaves</span>
            </div>
            <div class="dropdown-item" onclick="triggerSearch('${query} in Tested Zari')">
              <span><strong>${e.target.value}</strong> with Certified Silver Zari</span>
              <span style="font-size:11px;color:#8C6E18;">18 Weaves</span>
            </div>
            <div class="dropdown-item" onclick="triggerSearch('${query} Banarasi')">
              <span><strong>${e.target.value}</strong> in Banarasi Katan Silk</span>
              <span style="font-size:11px;color:#8C6E18;">29 Weaves</span>
            </div>
          `;
        }
      }
    });

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
        searchDropdown.classList.remove('active');
      }
    });
  }

  window.triggerSearch = (keyword) => {
    if (searchInput) searchInput.value = keyword;
    if (searchDropdown) searchDropdown.classList.remove('active');
    showToast(`Filtering collection for: "${keyword}"`);
  };

  // -------------------------------------------------------------------------
  // 4. Modal Management System
  // -------------------------------------------------------------------------
  const appointmentModal = document.getElementById('appointment-modal');
  const quickViewModal = document.getElementById('quick-view-modal');
  const storeModal = document.getElementById('store-modal');

  function openModal(modal) {
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeModal(overlay);
      }
    });
  });

  document.querySelectorAll('.modal-close-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-overlay');
      closeModal(modal);
    });
  });

  // Open Appointment Modal
  const bookBtns = document.querySelectorAll('.trigger-appointment');
  bookBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(appointmentModal);
    });
  });

  // Time slot selection pills
  document.querySelectorAll('.slot-pill').forEach(pill => {
    pill.addEventListener('click', function() {
      document.querySelectorAll('.slot-pill').forEach(p => p.classList.remove('selected'));
      this.classList.add('selected');
    });
  });

  // Appointment Form Submit
  const appointmentForm = document.getElementById('appointment-form');
  if (appointmentForm) {
    appointmentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('appt-name').value;
      const phone = document.getElementById('appt-phone').value;
      const slot = document.querySelector('.slot-pill.selected')?.textContent || '11:00 AM IST';
      
      closeModal(appointmentModal);
      showToast(`Appointment Confirmed for ${name}! Loom specialist slot: ${slot}`);
      appointmentForm.reset();
    });
  }

  // -------------------------------------------------------------------------
  // 5. Hero Product Quick View & Swatch Zoom
  // -------------------------------------------------------------------------
  const heroProductHotspot = document.getElementById('hero-product-trigger');
  if (heroProductHotspot) {
    heroProductHotspot.addEventListener('click', () => {
      openModal(quickViewModal);
    });
  }

  const heroSwatchHotspot = document.getElementById('hero-swatch-trigger');
  if (heroSwatchHotspot) {
    heroSwatchHotspot.addEventListener('click', () => {
      showToast('Zari Purity Assay: 100% Tested Silver-Gilt Weft, 24K Gold Plated Luster');
    });
  }

  // -------------------------------------------------------------------------
  // 6. Slide-Over Drawers (Cart, Wishlist, WhatsApp)
  // -------------------------------------------------------------------------
  const drawerOverlay = document.getElementById('drawer-overlay');
  const cartDrawer = document.getElementById('cart-drawer');
  const wishlistDrawer = document.getElementById('wishlist-drawer');
  const whatsappDrawer = document.getElementById('whatsapp-drawer');

  function openDrawer(drawer) {
    if (!drawer || !drawerOverlay) return;
    drawerOverlay.classList.add('active');
    drawer.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeAllDrawers() {
    if (drawerOverlay) drawerOverlay.classList.remove('active');
    document.querySelectorAll('.drawer-container').forEach(d => d.classList.remove('active'));
    document.body.style.overflow = '';
  }

  if (drawerOverlay) {
    drawerOverlay.addEventListener('click', closeAllDrawers);
  }

  document.querySelectorAll('.drawer-close-btn').forEach(btn => {
    btn.addEventListener('click', closeAllDrawers);
  });

  // Cart Button
  const cartBtn = document.getElementById('cart-btn');
  if (cartBtn) {
    cartBtn.addEventListener('click', () => openDrawer(cartDrawer));
  }

  // Wishlist Button
  const wishlistBtn = document.getElementById('wishlist-btn');
  if (wishlistBtn) {
    wishlistBtn.addEventListener('click', () => openDrawer(wishlistDrawer));
  }

  // WhatsApp Stylist Trigger
  const whatsappBtns = document.querySelectorAll('.trigger-whatsapp');
  whatsappBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openDrawer(whatsappDrawer);
    });
  });

  // Store Locator Trigger
  const storeTrigger = document.getElementById('store-locator-btn');
  if (storeTrigger) {
    storeTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(storeModal);
    });
  }

  // Currency Selector Button
  const currencyBtn = document.getElementById('currency-selector-btn');
  const currencyDropdown = document.getElementById('currency-dropdown');
  if (currencyBtn && currencyDropdown) {
    currencyBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      currencyDropdown.classList.toggle('active');
    });

    document.querySelectorAll('.currency-option').forEach(opt => {
      opt.addEventListener('click', () => {
        const curr = opt.getAttribute('data-currency');
        updatePrices(curr);
        currencyDropdown.classList.remove('active');
      });
    });

    document.addEventListener('click', () => {
      currencyDropdown.classList.remove('active');
    });
  }

  // Mobile Menu Drawer Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-toggle');
  const mobileNavDrawer = document.getElementById('mobile-nav-drawer');
  if (mobileMenuBtn && mobileNavDrawer) {
    mobileMenuBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      openDrawer(mobileNavDrawer);
    });
  }

  // Mobile Search Toggle
  const mobileSearchToggle = document.getElementById('mobile-search-toggle');
  const mobileSearchBar = document.getElementById('mobile-search-bar');
  const mobileSearchInput = document.getElementById('mobile-search-input');
  if (mobileSearchToggle && mobileSearchBar) {
    mobileSearchToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      mobileSearchBar.classList.toggle('active');
      if (mobileSearchBar.classList.contains('active') && mobileSearchInput) {
        mobileSearchInput.focus();
      }
    });
  }

  if (mobileSearchInput) {
    mobileSearchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const query = mobileSearchInput.value.trim();
        if (query) {
          triggerSearch(query);
          mobileSearchBar.classList.remove('active');
        }
      }
    });
  }

  // -------------------------------------------------------------------------
  // 7. Interactive Toast Notification System
  // -------------------------------------------------------------------------
  function showToast(message) {
    let container = document.getElementById('toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toast-container';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast-card';
    toast.innerHTML = `
      <span style="color:var(--color-gold-light); font-size:12px;">&bull;</span>
      <span>${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 300);
    }, 3800);
  }

  window.showToast = showToast;

  // Add to Bag action inside Quick View
  const addToBagBtn = document.getElementById('quick-add-to-bag');
  if (addToBagBtn) {
    addToBagBtn.addEventListener('click', () => {
      closeModal(quickViewModal);
      const cartCountEl = document.getElementById('cart-count');
      if (cartCountEl) {
        const currentCount = parseInt(cartCountEl.textContent || '2');
        cartCountEl.textContent = currentCount + 1;
      }
      showToast('Added "The Rudraksha Mayil Kanchipuram" to your Shopping Bag!');
    });
  }

  // WhatsApp Message Send in drawer
  const whatsappSendBtn = document.getElementById('whatsapp-send-btn');
  const whatsappInput = document.getElementById('whatsapp-input');
  const whatsappChatBox = document.getElementById('whatsapp-messages');

  if (whatsappSendBtn && whatsappInput && whatsappChatBox) {
    whatsappSendBtn.addEventListener('click', () => {
      const msg = whatsappInput.value.trim();
      if (!msg) return;

      const userBubble = document.createElement('div');
      userBubble.style.cssText = 'background:#E7FFDB; padding:10px 14px; border-radius:10px; margin-bottom:10px; align-self:flex-end; max-width:80%; font-size:13px; color:#111; box-shadow:0 1px 3px rgba(0,0,0,0.1);';
      userBubble.textContent = msg;
      whatsappChatBox.appendChild(userBubble);
      whatsappInput.value = '';
      whatsappChatBox.scrollTop = whatsappChatBox.scrollHeight;

      setTimeout(() => {
        const stylistBubble = document.createElement('div');
        stylistBubble.style.cssText = 'background:#FFFFFF; padding:10px 14px; border-radius:10px; margin-bottom:10px; align-self:flex-start; max-width:85%; font-size:13px; color:#111; border:1px solid #E6E1DC; box-shadow:0 1px 3px rgba(0,0,0,0.06);';
        stylistBubble.innerHTML = '<strong>Stylist Ananya:</strong> Namaste! I am pulling up our tested zari 2025 Sovereign edit drapes for you. Would you like a high-definition video walkthrough or photo catalog?';
        whatsappChatBox.appendChild(stylistBubble);
        whatsappChatBox.scrollTop = whatsappChatBox.scrollHeight;
      }, 1000);
    });
  }

  // Global handlers for section triggers
  window.openProductQuickView = (title, price, desc) => {
    const titleEl = document.getElementById('qv-title');
    const priceEl = document.getElementById('qv-price');
    const descEl = document.getElementById('qv-desc');
    if (titleEl) titleEl.textContent = title;
    if (priceEl) {
      priceEl.setAttribute('data-inr-price', price);
      updatePrices(currentCurrency);
    }
    if (descEl) descEl.textContent = desc;
    openModal(quickViewModal);
  };

  window.openVideoLoomModal = () => {
    showToast('Launching 4K Handloom Documentary: The 45-Year Sacred Guild');
  };

  window.subscribeNewsletter = () => {
    const input = document.getElementById('newsletter-email');
    if (input && input.value) {
      showToast(`Thank you! Privileged Sovereign invitations will be sent to ${input.value}`);
      input.value = '';
    } else {
      showToast('Please enter a valid email address.');
    }
  };

  window.closeModal = closeModal;
  window.openModal = openModal;

  // Header Sticky Elevation
  window.addEventListener('scroll', () => {
    const header = document.querySelector('.site-header');
    if (header) {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
  });
});
