import React, { useState } from 'react'
import JsonData from './data.json'
// import component
import TextField from '@mui/material/TextField';
import Table from '@mui/material/Table';

import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';

function useInput({ type, id, label }) {
 const [value, setValue] = useState("");
 const input = <TextField id={id} label={label} variant="filled" value={value} onChange={e => setValue(e.target.value)} type={type} />;
 return [value, input];
}

function JsonDataDisplay() {
 const [department_input, department] = useInput({ type: "text", id: "department-id", label: "Department" });
 const [university_input, university] = useInput({ type: "text", id: "university", label: "University" });
 return (
  <div>
  <Box
   component="form"
   sx={{
    '& > :not(style)': { m: 1, width: '25ch' },
   }}
   noValidate
   autoComplete="off">
   {university}
   {department}
  </Box>
  <TableContainer component={Paper}>
   <Table sx={{ minWidth: 650 }} aria-label="simple table">

    <TableHead>
     <TableRow>
      <TableCell>Name</TableCell>
      <TableCell>Email</TableCell>
      <TableCell>Research Interests</TableCell>
      <TableCell>University</TableCell>
      <TableCell>Department</TableCell>
     </TableRow>
    </TableHead>

    <TableBody>
     {JsonData
      // traverse data, each professor' information matches the two input values
      .filter((row) => row.department === department_input && row.university === university_input)
      .map((row) => (
       <TableRow
        key={row.name}
        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
       >
        <TableCell component="th" scope="row">{row.name}</TableCell>
        <TableCell>{row.email}</TableCell>
        <TableCell>{row.research_interests}</TableCell>
        <TableCell>{row.university}</TableCell>
        <TableCell>{row.department}</TableCell>
       </TableRow>
      ))}
    </TableBody>
   </Table>
  </TableContainer>
  </div>
 )
}

const Display = () => {
 return (
  <React.Fragment>
   <JsonDataDisplay />
  </React.Fragment>
 );
};

export default Display;