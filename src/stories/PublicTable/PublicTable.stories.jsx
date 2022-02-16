import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import PublicTable from './PublicTable';

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Tabla de filtro publico',
  component: PublicTable,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Tabla_filtro_publico = (args) => {
return <PublicTable />;
}