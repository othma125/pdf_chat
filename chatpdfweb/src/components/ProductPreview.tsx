import React from "react";
import Image from "next/image";
import Link from "next/link";

type Props = {};

const ProductPreview = (props: Props) => {
  return (
    <div>
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="mt-16 flow-root sm:mt-24">
          <div className="-m-2 rounded-xl bg-gray-900/5 p-2 ring-1 ring-inset ring-gray-900/10 lg:-m-4 lg:rounded-2xl lg:p-4">
            <Image
              src="/dashboard-preview.jpg"
              alt="product preview"
              width={1364}
              height={866}
              quality={100}
              className="rounded-md bg-white p-2 sm:p-8 md:p-20 shadow-2xl ring-1 ring-gray-900/10"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductPreview;
