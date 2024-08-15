import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CheckboxList = () => {
  const [checkedItems, setCheckedItems] = useState({});
  const [foodItems, setFoodItems] = useState([]);
  const [names, setNames] = useState([]);
  const [newName, setNewName] = useState('');
  const [selectedNames, setSelectedNames] = useState({});
  const [submittedData, setSubmittedData] = useState(null);
  const [newCheckbox, setNewCheckbox] = useState('');
  const [owedAmounts, setOwedAmounts] = useState({});
  const [loading, setLoading] = useState(false);

  // Fetch food items from API and update checkedItems
  const getItems = () => {
    fetch('http://127.0.0.1:5000/getFoods')
      .then(response => {
        if (!response.ok) {
          throw new Error('Item Not Found');
        }
        return response.json(); // Convert response to JSON
      })
      .then(data => {
        setFoodItems(data);
        // Update checkedItems state
        const updatedCheckedItems = data.reduce((acc, item) => {
          acc[item] = false; // Initialize each item as unchecked
          return acc;
        }, {});
        setCheckedItems(updatedCheckedItems);
      })
      .catch(error => {
        console.error('No Food Items Returned:', error);
        setFoodItems({ error: 'Item not found' });
      });
  };

  useEffect(() => {
    getItems(); // Fetch items when component mounts
  }, []);

  const handleChange = (event) => {
    setCheckedItems({
      ...checkedItems,
      [event.target.name]: event.target.checked,
    });
    console.log(event.target.name + " was checked!")
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Food Items Ordered:', checkedItems);
  };

  const handleNameChange = (event) => {
    setNewName(event.target.value);
  };

  const handleNameSubmit = (event) => {
    event.preventDefault();
    if (newName.trim() && !names.includes(newName)) {
      setNames([...names, newName]);
      setSelectedNames({ ...selectedNames, [newName]: [] });
      setNewName('');
    }
    addingPerson();
  }

  const addingPerson = async () =>{
    const response = await axios.post('http://localhost:5000/addPerson', {name: newName});
  }

  // Final checkbox handler
  const handleNameCheckboxChange = (event, itemName) => {
    const { name, checked } = event.target;
    setSelectedNames((prevSelectedNames) => {
      const updatedNames = { ...prevSelectedNames };
      if (checked) {
        updatedNames[name].push(itemName);
      } else {
        updatedNames[name] = updatedNames[name].filter((item) => item !== itemName);
      }
      console.log(name + " bought " + itemName)
      return updatedNames;
    });

  };

  // Final submit handler
  const handleFinalSubmit = async (event) => {
    event.preventDefault();

    // enable the loading sign
    setLoading(true);

    setSubmittedData(selectedNames);
    console.log('Selected items by name:', selectedNames);

    // Updates the ordered for all of the people with checked off checkboxes
    try {
      const response = await axios.put('http://localhost:5000/updateOrdered', selectedNames);
      console.log(response.data);
    } catch (error) {
      console.error('Error updating ordered items:', error);
    }

    // Updates the owed for all of the people with checked off checkboxes
    // Grabs the items that they bought and extracts the prices, adding it to their total
    try {
      const response = await axios.put('http://localhost:5000/updateOwed', selectedNames);
      console.log(response.data);
    } catch (error) {
      console.error('Error updating ordered items:', error);
    }

    const owedAmountsTemp = {};
    for (const name of Object.keys(selectedNames)) {
      try {
        const response = await axios.get('http://localhost:5000/getOwed', {params:{name: name}} );
        owedAmountsTemp[name] = response.data.owed;
        console.log(response.data)
      } catch (error) {
        console.error(`Error getting owed amount for ${name}:`, error);
        owedAmountsTemp[name] = 'Error';
      }
    }
    setOwedAmounts(owedAmountsTemp);

    // remove loading and show owed values
    setLoading(false);

  };

  const handleAddCheckbox = (event) => {
    event.preventDefault();
    if (newCheckbox.trim() && !checkedItems.hasOwnProperty(newCheckbox)) {
      setCheckedItems({
        ...checkedItems,
        [newCheckbox]: false,
      });
      setNewCheckbox('');
    }
  };

  const handleNewCheckboxChange = (event) => {
    setNewCheckbox(event.target.value);
  };

  return (
    <div>
      <h1>Which parts of the reciept were bought by everyone?</h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(checkedItems).map((item) => ( 
            <div key={item}>
                <label>
                <input
                    type="checkbox"
                    name={item}
                    checked={checkedItems[item]}
                    onChange={handleChange}
                />
                {item.charAt(0).toUpperCase() + item.slice(1)}
                </label>
            </div>
            
        ))}
        <button type="submit">Submit</button>
      </form>

      <h2>Add Items to Receipt</h2>
      <form onSubmit={handleAddCheckbox}>
        <input
          type="text"
          value={newCheckbox}
          onChange={handleNewCheckboxChange}
          placeholder="Enter item"
        />
        <button type="submit">Add Item</button>
      </form>
      
      <h2>Add Names</h2>
      <form method = "POST" onSubmit={handleNameSubmit}>
        <input
          type="text"
          name = "addPerson"
          value={newName}
          onChange={handleNameChange}
          placeholder="Enter name"
        />
        <button type="submit">Add Name</button>
      </form>

      <h2>Names and Items</h2>
      <form onSubmit={handleFinalSubmit}>
      {names.map((name) => (
        <div key={name}>
          <h3>{name}</h3>
          {Object.keys(checkedItems).map((item) => (
            checkedItems[item] && (
                <div key={item}>
                <label>
                    <input
                    type="checkbox"
                    name={name}
                    checked={selectedNames[name]?.includes(item)}
                    onChange={(e) => handleNameCheckboxChange(e, item)}
                    />
                    {item.charAt(0).toUpperCase() + item.slice(1)}
                </label>
                </div>
            )
          ))}
        </div>
      ))}
        <button type="submit">Submit Peoples' Purchased Items</button>
      </form>
    
        <div style={{ flex: 1, marginLeft: '20px' }}>
            <h2>Total Payments: </h2>
            {/* ADDED FOR LOADING ALL AT ONCE PURPOSES */}
            {loading ? (
          <div>Loading...</div>
            ) : (
          submittedData && Object.keys(submittedData).map((name) => (
            <div key={name}>
              <strong>{name}:</strong> {owedAmounts[name]}
            </div>
          ))
        )}
      </div>
    </div>
  );
};
export default CheckboxList;