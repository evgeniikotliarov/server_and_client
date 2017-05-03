CONTINUE = b'100', b'Continue'
SWITCHING_PROTOCOLS = b'101', b'Switching Protocols'
PROCESSING = b'102', b'Processing'

# success
OK = b'200', b'OK'
CREATED = b'201', b'Created'
ACCEPTED = b'202', b'Accepted'
NO_CONTENT = b'204', b'No Content'
RESET_CONTENT = b'205', b'Reset Content'
PARTIAL_CONTENT = b'206', b'Partial Content'
MULTI_STATUS = b'207', b'Multi-Status'
ALREADY_REPORTED = b'208', b'Already Reported'
IM_USED = b'226', b'IM Used'

# redirection
MULTIPLE_CHOICES = b'300', b'Multiple Choices'
MOVED_PERMANENTLY = b'301', b'Moved Permanently'
FOUND = b'302', b'Found'
SEE_OTHER = b'303', b'See Other'
NOT_MODIFIED = b'304', b'Not Modified'
USE_PROXY = b'305', b'Use Proxy'
TEMPORARY_REDIRECT = b'307', b'Temporary Redirect'
PERMANENT_REDIRECT = b'308', b'Permanent Redirect'

# client error
BAD_REQUEST = b'400', b'Bad Request'
UNAUTHORIZED = b'401', b'Unauthorized'
FORBIDDEN = b'403', b'Forbidden'
NOT_FOUND = b'404', b'Not Found'
METHOD_NOT_ALLOWED = b'405', b'Method Not Allowed'
NOT_ACCEPTABLE = b'406', b'Not Acceptable'
REQUEST_TIMEOUT = b'408', b'Request Timeout'
CONFLICT = b'409', b'Conflict'
GONE = b'410', b'Gone'
LENGTH_REQUIRED = b'411', b'Length Required'
PRECONDITION_FAILED = b'412', b'Precondition Failed',
REQUEST_ENTITY_TOO_LARGE = b'413', b'Request Entity Too Large',
REQUEST_URI_TOO_LONG = b'414', b'Request-URI Too Long',
UNSUPPORTED_MEDIA_TYPE = b'415', b'Unsupported Media Type',
REQUESTED_RANGE_NOT_SATISFIABLE = b'416', b'Requested Range Not Satisfiable'
EXPECTATION_FAILED = b'417', b'Expectation Failed'
UPGRADE_REQUIRED = b'426', b'Upgrade Required'
PRECONDITION_REQUIRED = b'428', b'Precondition Required',
TOO_MANY_REQUESTS = b'429', b'Too Many Requests',
REQUEST_HEADER_FIELDS_TOO_LARGE = b'431', b'Request Header Fields Too Large'

# server errors
INTERNAL_SERVER_ERROR = b'500', b'Internal Server Error',
NOT_IMPLEMENTED = b'501', b'Not Implemented',
BAD_GATEWAY = b'502', b'Bad Gateway',
SERVICE_UNAVAILABLE = b'503', b'Service Unavailable',
GATEWAY_TIMEOUT = b'504', b'Gateway Timeout',
HTTP_VERSION_NOT_SUPPORTED = b'505', b'HTTP Version Not Supported',
VARIANT_ALSO_NEGOTIATES = b'506', b'Variant Also Negotiates'
INSUFFICIENT_STORAGE = b'507', b'Insufficient Storage'
LOOP_DETECTED = b'508', b'Loop Detected'
NOT_EXTENDED = b'510', b'Not Extended'
NETWORK_AUTHENTICATION_REQUIRED = b'511', b'Network Authentication Required'
