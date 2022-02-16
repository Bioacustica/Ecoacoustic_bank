import React from 'react';
import AdministratorNavbar from './AdministratorNavbar';
import { CustomDocumentationComponent } from './documentacion';



// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Barra de navegacion administrador',
  component: AdministratorNavbar,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Administrador = (args) => {
return <AdministratorNavbar />;
}