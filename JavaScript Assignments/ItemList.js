import React from 'react';

function ItemList(props) {
  const { items } = props;

  return (
    <ol>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ol>
  );
}

export default ItemList;
