CONTINUE = 100, b'Continue'
SWITCHING_PROTOCOLS = 101, b'Switching Protocols'
PROCESSING = 102, b'Processing'

# success
OK = b'200', b'OK'
CREATED = 201, b'Created'
ACCEPTED = 202, b'Accepted'
NO_CONTENT = 204, b'No Content'
RESET_CONTENT = 205, b'Reset Content'
PARTIAL_CONTENT = 206, b'Partial Content'
MULTI_STATUS = 207, b'Multi-Status'
ALREADY_REPORTED = 208, b'Already Reported'
IM_USED = 226, b'IM Used'

# redirection
MULTIPLE_CHOICES = 300, b'Multiple Choices'
MOVED_PERMANENTLY = 301, b'Moved Permanently'
FOUND = 302, b'Found'
SEE_OTHER = 303, b'See Other'
NOT_MODIFIED = 304, b'Not Modified'
USE_PROXY = 305, b'Use Proxy'
TEMPORARY_REDIRECT = 307, b'Temporary Redirect'
PERMANENT_REDIRECT = 308, b'Permanent Redirect'

# client error
BAD_REQUEST = 400, b'Bad Request'
UNAUTHORIZED = 401, b'Unauthorized'
FORBIDDEN = 403, b'Forbidden'
NOT_FOUND = 404, b'Not Found'
METHOD_NOT_ALLOWED = 405, b'Method Not Allowed'
NOT_ACCEPTABLE = 406, b'Not Acceptable'
REQUEST_TIMEOUT = 408, b'Request Timeout'
CONFLICT = 409, b'Conflict', 'Request conflict'
GONE = 410, b'Gone'
LENGTH_REQUIRED = 411, b'Length Required'
PRECONDITION_FAILED = 412, b'Precondition Failed',
REQUEST_ENTITY_TOO_LARGE = 413, b'Request Entity Too Large',
REQUEST_URI_TOO_LONG = 414, b'Request-URI Too Long',
UNSUPPORTED_MEDIA_TYPE = 415, b'Unsupported Media Type',
REQUESTED_RANGE_NOT_SATISFIABLE = 416, b'Requested Range Not Satisfiable'
EXPECTATION_FAILED = 417, b'Expectation Failed'
UPGRADE_REQUIRED = 426, b'Upgrade Required'
PRECONDITION_REQUIRED = 428, b'Precondition Required',
TOO_MANY_REQUESTS = 429, b'Too Many Requests',
REQUEST_HEADER_FIELDS_TOO_LARGE = 431, b'Request Header Fields Too Large'

# server errors
INTERNAL_SERVER_ERROR = 500, b'Internal Server Error',
NOT_IMPLEMENTED = 501, b'Not Implemented',
BAD_GATEWAY = 502, b'Bad Gateway',
SERVICE_UNAVAILABLE = 503, b'Service Unavailable',
GATEWAY_TIMEOUT = 504, b'Gateway Timeout',
HTTP_VERSION_NOT_SUPPORTED = 505, b'HTTP Version Not Supported',
VARIANT_ALSO_NEGOTIATES = 506, b'Variant Also Negotiates'
INSUFFICIENT_STORAGE = 507, b'Insufficient Storage'
LOOP_DETECTED = 508, b'Loop Detected'
NOT_EXTENDED = 510, b'Not Extended'
NETWORK_AUTHENTICATION_REQUIRED = 511, b'Network Authentication Required'