import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./App.css"

const Dashboard = () => {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState('');
  const [gender, setGender] = useState('');
  const [university, setUniversity] = useState('');
  const [phone, setPhone] = useState('');
  const [editingUserId, setEditingUserId] = useState(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get('http://localhost:8000/users/');
      setUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const addUser = async () => {
    try {
      const response = await axios.post('http://localhost:8000/users/', {
        name,
        gender,
        university,
        phone,
      });
      setUsers([...users, response.data]);
    } catch (error) {
      console.error('Error adding user:', error);
    }
  };

  const deleteUser = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/users/${id}`);
      setUsers(users.filter((user) => user.id !== id));
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  const updateUser = async (id) => {
    try {
      await axios.put(`http://localhost:8000/users/${id}`, {
        name,
        gender,
        university,
        phone,
      });
      // Update the user list after successful update
      const updatedUsers = users.map((user) =>
        user.id === id ? { ...user, name, gender, university, phone } : user
      );
      setUsers(updatedUsers);
      // Reset input fields and editing state
      setName('');
      setGender('');
      setUniversity('');
      setPhone('');
      setEditingUserId(null);
    } catch (error) {
      console.error('Error updating user:', error);
    }
  };

  const startEditingUser = (user) => {
    // Set input fields with user's current data
    setName(user.name);
    setGender(user.gender);
    setUniversity(user.university);
    setPhone(user.phone);
    // Set editing state
    setEditingUserId(user.id);
  };

  const cancelEditing = () => {
    // Reset input fields and editing state
    setName('');
    setGender('');
    setUniversity('');
    setPhone('');
    setEditingUserId(null);
  };

  return (
    <div>
      <h1>VDT</h1>
      <div>
        <h2>{editingUserId ? 'Edit User' : 'Add User'}</h2>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Gender"
          value={gender}
          onChange={(e) => setGender(e.target.value)}
        />
        <input
          type="text"
          placeholder="University"
          value={university}
          onChange={(e) => setUniversity(e.target.value)}
        />
        <input
          type="text"
          placeholder="Phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
        {editingUserId ? (
          <>
            <button onClick={() => updateUser(editingUserId)}>Update</button>
            <button onClick={cancelEditing}>Cancel</button>
          </>
        ) : (
          <button onClick={addUser}>Add User</button>
        )}
      </div>
      <div>
        <h2>Users</h2>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Gender</th>
              <th>University</th>
              <th>Phone</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.gender}</td>
                <td>{user.university}</td>
                <td>{user.phone}</td>
                <td>
                  <button onClick={() => startEditingUser(user)}>Edit</button>
                  <button onClick={() => deleteUser(user.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
