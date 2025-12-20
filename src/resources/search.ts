// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class Search extends APIResource {
  /**
   * Query the AI for media exploration and recommendations
   */
  recommend(options?: RequestOptions): APIPromise<SearchRecommendResponse> {
    return this._client.post('/search', options);
  }
}

export interface SearchRecommendResponse {
  result: string;
}

export declare namespace Search {
  export { type SearchRecommendResponse as SearchRecommendResponse };
}
