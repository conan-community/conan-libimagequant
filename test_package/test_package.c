#include <stdio.h>
#include "libimagequant.h"

int main() {
    printf("imagequant version: %d\n", liq_version());

    liq_attr *handle = liq_attr_create();
    liq_histogram *histogram = liq_histogram_create(handle);

    liq_histogram_destroy(histogram);
    liq_attr_destroy(handle);

    return 0;
}
