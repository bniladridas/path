// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import type { Harper } from '../client';

export abstract class APIResource {
  protected _client: Harper;

  constructor(client: Harper) {
    this._client = client;
  }
}
