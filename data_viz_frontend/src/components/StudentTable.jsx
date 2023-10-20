import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button } from '@mui/material';
import { useState,useEffect, useRef } from 'react';



function createData(id , student) {
    return { id , student};
  }
  
  let rows = [];
  
  export default function StudentTable() {

    const [fetchedData, setFetchedData] = useState(0)
    const fromIndex = useRef({
      index: 0
    })
    const toIndex = useRef({
      index: 100
    })
 
    const fetchRows = () => 
    {

      let url = "http://127.0.0.1:8000/home/?category=students&from=" + fromIndex.current.index + "&to=" + toIndex.current.index;
      fetch(url)
        .then(response => {
          console.log(url);

          return response.json();
        })
        .then(data => {
          // rows = []
          data.forEach(element => {
            rows.push(createData(element.pk , element.fields.student_name))
            
          });
          fromIndex.current.index = toIndex.current.index;
          toIndex.current.index = toIndex.current.index + 100;
          console.log(fromIndex.current.index , toIndex.current.index)
          setFetchedData(toIndex.current.index)
        })
    }

    return (
      <div>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Student Id</TableCell>
              <TableCell align="right">Student Name</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.id}
                </TableCell>
                <TableCell align="right">{row.student}</TableCell>

              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Button variant="text" fullWidth onClick={fetchRows}>Fetch Data</Button>
      </div>
    );

}