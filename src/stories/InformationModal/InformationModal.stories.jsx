import React from 'react';
import { CustomDocumentationComponent } from './documentacion';
import MoreInformationModal from './MoreInformationModal';






// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: 'Bioacustica/Modal de mas informacion',
  component: MoreInformationModal,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  parameters:{
      docs:{
          page: CustomDocumentationComponent
      }
  }
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
export const Modal_de_mas_informacion= (args) => {
return <MoreInformationModal />;
}