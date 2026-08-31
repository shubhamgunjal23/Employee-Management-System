import http from 'k6/http';
import { check, sleep } from 'k6';
export const options={stages:[
 {duration:'30s',target:10},{duration:'60s',target:50},
 {duration:'60s',target:100},{duration:'30s',target:0}]};
export default function(){
 const r=http.get(`${__ENV.BASE_URL}/health`);
 check(r,{'status 200':x=>x.status===200}); sleep(1);
}
