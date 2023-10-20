import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import SchoolTable from './SchoolTable';
import AnswerTable from './AnswerTable';
import StudentTable from './StudentTable';
import AwardTable from './AwardTable';
import AssessmentAreaTable from './AssessmentAreaTable';
import SubjectTable from './SubjectTable';
import ClassTable from './ClassTable';
import SummaryTable from './SummaryTable';


function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {children}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function BasicTabs() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
          <Tab label="School" {...a11yProps(0)} />
          <Tab label="Students" {...a11yProps(1)} />
          <Tab label="Answers" {...a11yProps(2)} />
          <Tab label="Assessment Areas" {...a11yProps(3)} />
          <Tab label="Awards" {...a11yProps(4)} />
          <Tab label="Subject" {...a11yProps(5)} />
          <Tab label="Class" {...a11yProps(6)} />
          <Tab label="Summary" {...a11yProps(7)} />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        <SchoolTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <StudentTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        <AnswerTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={3}>
        <AssessmentAreaTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={4}>
        <AwardTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={5}>
        <SubjectTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={6}>
        <ClassTable/>
      </CustomTabPanel>
      <CustomTabPanel value={value} index={7}>
        <SummaryTable/>
      </CustomTabPanel>
    </Box>
  );
}
