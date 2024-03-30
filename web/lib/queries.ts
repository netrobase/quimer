import { gql } from '@apollo/client';
import { USER_FRAGMENT } from './fragments';

export const FETCH_USER_QUERY = gql`
  ${USER_FRAGMENT}
  query FetchUser($userId: Int!) {
    users(id: $userId) {
      ...UserFragment
    }
  } 
`;