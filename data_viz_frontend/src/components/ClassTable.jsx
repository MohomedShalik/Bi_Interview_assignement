import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useState ,useEffect} from 'react';



function createData(id , class_name) {
    return { id , class_name};
  }
  
  let rows = [];
  
  export default function ClassTable() {

    const [fetchedData, setFetchedData] = useState(false)


    useEffect(() => {
      fetchUserData();
    }, [fetchedData]);

    const fetchUserData = () => {
      fetch("http://127.0.0.1:8000//home/?category=class")
        .then(response => {
          return response.json()
        })
        .then(data => {
          rows = []
          console.log(data[0].fields)
          data.forEach(element => {
            rows.push(createData(element.pk , element.fields.class_name))
            setFetchedData(true)
          });
        })
    }


    return (
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Class Id</TableCell>
              <TableCell align="right">Class</TableCell>
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
                <TableCell align="right">{row.class_name}</TableCell>

              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );

}