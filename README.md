# kereby-apartment-service

This is a filter/alert service I built for my sister to help her find an apartment on https://kereby.dk/
//
This service is integrated with AWS Lambda, Cloudwatch, and S3. I used Lambda to house the function that would send a GET request to kereby's API to get information on any existing or new listings. If any new listing or change to an existing listing that fits the filter my sister requested(2 bedrooms, 2 bath, etc.) an email would be sent to me as well as my sister. Cloudwatch manages the scheduled daily triggering of the Lambda function to ensure she is up to date with the latest information, and doesn't need to parse through the site herself every day. S3 stores all of the information obtained from the GET request sent in the Lambda function, allowing me to check for any changes or new listings in the first place.
//
This was my first foray into AWS tools and services, so I'm really happy that the results were tangible and I was able to help my sister get an apartment!
