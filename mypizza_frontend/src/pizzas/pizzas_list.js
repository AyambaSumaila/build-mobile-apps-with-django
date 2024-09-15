import React, { Component } from 'react';

import DummyData from './dummy.json';

class PizzaList extends React.Component {
    render()
     {

        return (


            <div>
                {DummyData.map(p =>

                    <h4>{p.pizzas} - {p.city} </h4>
                )}
                <h2>Pizza Name Goes here</h2>
            </div>
        )
    }

}

export default PizzaList;