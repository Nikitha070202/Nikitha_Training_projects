import React from 'react';

function Header(props) {
  const { title = 'Default Title', subtitle = 'Default Subtitle' } = props;

  return (
    <header>
      <h1>{title}</h1>
      <h2>{subtitle}</h2>
    </header>
  );
}

export default Header;
