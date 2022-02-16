import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import PublicFilter from "./PublicFilter"





// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Filtro Publico',
  component: PublicFilter,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Filtro_para_Publico = (args) => {
return <PublicFilter />;
}