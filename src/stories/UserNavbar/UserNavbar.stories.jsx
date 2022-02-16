import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import Navbar from './Navbar';






// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Barra de navegacion publica',
  component: Navbar,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Navbar_publica = (args) => {
return <Navbar />;
}