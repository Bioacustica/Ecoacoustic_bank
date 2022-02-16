import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import PrivateDonwloadFilter from './PrivateDonwloadFilter';




// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Filtro de descarga',
  component: PrivateDonwloadFilter,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Filtro_descarga = (args) => {
return <PrivateDonwloadFilter />;
}