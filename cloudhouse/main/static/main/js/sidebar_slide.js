const tabs = document.querySelectorAll('[data-tab-name]');
const tabContents = document.querySelectorAll('[data-tab-content]');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const tabName = tab.dataset.tabName;
    setActiveTab(tabName);
  });
});


function setActiveTab(tabName) {

  tabContents.forEach(content => {
    content.style.display = 'none';
    content.classList.remove('active');
  });

  const activeContent = document.querySelector(`[data-tab-content="${tabName}"]`);
  activeContent.style.display = 'block';
  activeContent.classList.add('active');

  tabs.forEach(tab => {
    tab.classList.remove('active');
  });

  const activeTab = document.querySelector(`[data-tab-name="${tabName}"]`);
  activeTab.classList.add('active');
}
