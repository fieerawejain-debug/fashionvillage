with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find the end of .footer-secure-tag
mark = '.footer-secure-tag {'
idx = css.find(mark)

if idx == -1:
    print('Could not find .footer-secure-tag in css/style.css!')
    exit(1)

# Find closing brace of .footer-secure-tag
close_idx = css.find('}', idx)
head = css[:close_idx + 1]

clean_tail = '''

/* --------------------------------------------------------------------------
   9. Mobile Search Bar Dropdown
   -------------------------------------------------------------------------- */
.mobile-search-toggle-btn {
  display: none;
}

.mobile-search-bar {
  display: none;
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border);
  padding: 10px 16px;
  position: relative;
  z-index: 89;
}

.mobile-search-bar.active {
  display: block;
}

/* --------------------------------------------------------------------------
   10. Comprehensive Luxury Responsive Breakpoints
   -------------------------------------------------------------------------- */
@media (max-width: 1024px) {
  .header-container {
    padding: 0 20px;
    gap: 14px;
  }

  .search-container {
    max-width: 280px;
  }

  .footer-main {
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    padding: 48px 24px;
  }
}

@media (max-width: 768px) {
  /* Announcement Bar */
  .top-announcement-bar {
    height: auto;
    padding: 6px 12px;
  }

  .announcement-text {
    font-size: 9.5px;
    letter-spacing: 0.5px;
    white-space: normal;
    text-align: center;
    line-height: 1.35;
  }

  .announcement-text .dot {
    display: none;
  }

  /* Sticky Header */
  .header-container {
    height: 58px;
    padding: 0 12px;
    gap: 8px;
  }

  .brand-name {
    font-size: 17px;
    letter-spacing: 0.5px;
    line-height: 1;
  }

  .brand-sub {
    font-size: 6.5px;
    letter-spacing: 1px;
    margin-top: 2px;
  }

  .search-container {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    flex-shrink: 0;
  }

  #store-locator-btn,
  .header-v-divider,
  #currency-selector-btn,
  .user-avatar-circle {
    display: none;
  }

  .mobile-search-toggle-btn {
    display: flex !important;
    width: 34px;
    height: 34px;
  }

  .icon-action-btn {
    width: 34px;
    height: 34px;
  }

  .header-nav-actions {
    gap: 6px;
    flex-shrink: 0;
  }

  /* Footer */
  .footer-main {
    grid-template-columns: 1fr;
    gap: 30px;
    padding: 36px 16px 28px;
  }

  .footer-brand-col {
    padding-right: 0;
  }

  .footer-bottom-inner {
    flex-direction: column;
    text-align: center;
    gap: 12px;
  }

  .footer-bottom-links {
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
  }

  /* Modals & Drawers */
  .modal-dialog {
    max-width: 95% !important;
    margin: 10px auto;
  }

  .drawer-container {
    max-width: 85% !important;
  }

  /* Category Pages Mobile */
  .page-hero {
    padding: 36px 16px 24px !important;
  }

  .page-title {
    font-size: 26px !important;
    line-height: 1.2 !important;
  }

  .page-desc {
    font-size: 13.5px !important;
    padding: 0 10px;
  }

  .products-grid {
    padding: 24px 0 !important;
    gap: 16px !important;
  }

  .prod-img-box {
    height: 260px !important;
  }
}

@media (max-width: 480px) {
  .drawer-container {
    max-width: 100% !important;
  }

  .vip-salon-form {
    flex-direction: column;
    gap: 8px;
  }

  .vip-salon-input {
    border-radius: 4px;
    width: 100%;
  }

  .vip-salon-btn {
    border-radius: 4px;
    width: 100%;
  }
}
'''

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(head + clean_tail)

print('css/style.css cleaned and unified successfully!')
