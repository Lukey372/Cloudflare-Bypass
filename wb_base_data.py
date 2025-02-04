from random import uniform
from datetime import datetime

def wbBaseData(domain, useragent):
    return {
    "0": ["length", "innerWidth", "innerHeight", "scrollX", "pageXOffset", "scrollY", "pageYOffset", "screenX", "screenY", "screenLeft", "screenTop", "orientation", "TEMPORARY", "d.softNavigations"],
    "1": ["PERSISTENT", "d.childElementCount", "d.ELEMENT_NODE", "d.DOCUMENT_POSITION_DISCONNECTED"],
    "2": ["d.ATTRIBUTE_NODE", "d.DOCUMENT_POSITION_PRECEDING"],
    "3": ["d.TEXT_NODE"],
    "4": ["n.deviceMemory", "d.CDATA_SECTION_NODE", "d.DOCUMENT_POSITION_FOLLOWING"],
    "5": ["n.maxTouchPoints", "d.ENTITY_REFERENCE_NODE"],
    "6": ["d.ENTITY_NODE"],
    "7": ["d.PROCESSING_INSTRUCTION_NODE"],
    "8": ["n.hardwareConcurrency", "d.COMMENT_NODE", "d.DOCUMENT_POSITION_CONTAINS"],
    "9": ["d.nodeType", "d.DOCUMENT_NODE"],
    "10": ["d.DOCUMENT_TYPE_NODE"],
    "11": ["d.DOCUMENT_FRAGMENT_NODE"],
    "12": ["d.NOTATION_NODE"],
    "16": ["d.DOCUMENT_POSITION_CONTAINED_BY"],
    "32": ["d.DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC"],
    "531": ["outerWidth"],
    "995": ["outerHeight"],
    "o": ["window", "self", "document", "location", "customElements", "history", "navigation", "locationbar", "menubar", "personalbar", "scrollbars", "statusbar", "toolbar", "frames", "top", "parent", "frameElement", "navigator", "external", "screen", "visualViewport", "clientInformation", "styleMedia", "trustedTypes", "performance", "crypto", "indexedDB", "sessionStorage", "localStorage", "scheduler", "speechSynthesis", "chrome", "caches", "cookieStore", "launchQueue", "privateAttribution", "globalThis", "JSON", "Math", "Intl", "Atomics", "Reflect", "console", "CSS", "WebAssembly", "GPUBufferUsage", "GPUColorWrite", "GPUMapMode", "GPUShaderStage", "GPUTextureUsage", "n.scheduling", "n.userActivation", "n.geolocation", "n.connection", "n.plugins", "n.mimeTypes", "n.webkitTemporaryStorage", "n.webkitPersistentStorage", "n.bluetooth", "n.storageBuckets", "n.clipboard", "n.credentials", "n.keyboard", "n.managed", "n.mediaDevices", "n.storage", "n.serviceWorker", "n.virtualKeyboard", "n.wakeLock", "n.contacts", "n.ink", "n.devicePosture", "n.locks", "n.mediaCapabilities", "n.mediaSession", "n.ml", "n.permissions", "n.presentation", "n.gpu", "n.usb", "n.xr", "n.userAgentData", "d.location", "d.implementation", "d.documentElement", "d.body", "d.head", "d.images", "d.embeds", "d.plugins", "d.links", "d.forms", "d.scripts", "d.defaultView", "d.anchors", "d.applets", "d.scrollingElement", "d.featurePolicy", "d.children", "d.firstElementChild", "d.lastElementChild", "d.activeElement", "d.styleSheets", "d.fonts", "d.timeline", "d.fragmentDirective", "d.childNodes", "d.firstChild", "d.lastChild"],
    "F": ["closed", "crossOriginIsolated", "credentialless", "n.pdfViewerEnabled", "n.webdriver", "d.xmlStandalone", "d.wasDiscarded", "d.prerendering", "d.fullscreen", "d.webkitIsFullScreen"],
    "x": ["opener", "onsearch", "onappinstalled", "onbeforeinstallprompt", "onbeforexrselect", "onabort", "onbeforeinput", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange", "onclick", "onclose", "oncontextlost", "oncontextmenu", "oncontextrestored", "oncuechange", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onemptied", "onended", "onerror", "onfocus", "onformdata", "oninput", "oninvalid", "onkeydown", "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart", "onmousedown", "onmouseenter", "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmousewheel", "onpause", "onplay", "onplaying", "onprogress", "onratechange", "onreset", "onresize", "onscroll", "onsecuritypolicyviolation", "onseeked", "onseeking", "onselect", "onslotchange", "onstalled", "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting", "onwebkitanimationend", "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkittransitionend", "onwheel", "onauxclick", "ongotpointercapture", "onlostpointercapture", "onpointerdown", "onpointermove", "onpointerrawupdate", "onpointerup", "onpointercancel", "onpointerover", "onpointerout", "onpointerenter", "onpointerleave", "onselectstart", "onselectionchange", "onanimationend", "onanimationiteration", "onanimationstart", "ontransitionrun", "ontransitionstart", "ontransitionend", "ontransitioncancel", "onafterprint", "onbeforeprint", "onbeforeunload", "onhashchange", "onlanguagechange", "onmessage", "onmessageerror", "onoffline", "ononline", "onpagehide", "onpageshow", "onpopstate", "onrejectionhandled", "onstorage", "onunhandledrejection", "onunload", "onorientationchange", "oncontentvisibilityautostatechange", "onoverscroll", "onscrollend", "ontimezonechange", "ondevicemotion", "ondeviceorientation", "ondeviceorientationabsolute", "onbeforematch", "onbeforetoggle", "ontouchcancel", "ontouchend", "ontouchmove", "ontouchstart", "n.doNotTrack", "d.doctype", "d.xmlEncoding", "d.xmlVersion", "d.currentScript", "d.onreadystatechange", "d.all", "d.onpointerlockchange", "d.onpointerlockerror", "d.onbeforecopy", "d.onbeforecut", "d.onbeforepaste", "d.onfreeze", "d.onprerenderingchange", "d.onresume", "d.onsearch", "d.onvisibilitychange", "d.onfullscreenchange", "d.onfullscreenerror", "d.webkitCurrentFullScreenElement", "d.webkitFullscreenElement", "d.onwebkitfullscreenchange", "d.onwebkitfullscreenerror", "d.rootElement", "d.onbeforexrselect", "d.onabort", "d.onbeforeinput", "d.onblur", "d.oncancel", "d.oncanplay", "d.oncanplaythrough", "d.onchange", "d.onclick", "d.onclose", "d.oncontextlost", "d.oncontextmenu", "d.oncontextrestored", "d.oncuechange", "d.ondblclick", "d.ondrag", "d.ondragend", "d.ondragenter", "d.ondragleave", "d.ondragover", "d.ondragstart", "d.ondrop", "d.ondurationchange", "d.onemptied", "d.onended", "d.onerror", "d.onfocus", "d.onformdata", "d.oninput", "d.oninvalid", "d.onkeydown", "d.onkeypress", "d.onkeyup", "d.onload", "d.onloadeddata", "d.onloadedmetadata", "d.onloadstart", "d.onmousedown", "d.onmouseenter", "d.onmouseleave", "d.onmousemove", "d.onmouseout", "d.onmouseover", "d.onmouseup", "d.onmousewheel", "d.onpause", "d.onplay", "d.onplaying", "d.onprogress", "d.onratechange", "d.onreset", "d.onresize", "d.onscroll", "d.onsecuritypolicyviolation", "d.onseeked", "d.onseeking", "d.onselect", "d.onslotchange", "d.onstalled", "d.onsubmit", "d.onsuspend", "d.ontimeupdate", "d.ontoggle", "d.onvolumechange", "d.onwaiting", "d.onwebkitanimationend", "d.onwebkitanimationiteration", "d.onwebkitanimationstart", "d.onwebkittransitionend", "d.onwheel", "d.onauxclick", "d.ongotpointercapture", "d.onlostpointercapture", "d.onpointerdown", "d.onpointermove", "d.onpointerrawupdate", "d.onpointerup", "d.onpointercancel", "d.onpointerover", "d.onpointerout", "d.onpointerenter", "d.onpointerleave", "d.onselectstart", "d.onselectionchange", "d.onanimationend", "d.onanimationiteration", "d.onanimationstart", "d.ontransitionrun", "d.ontransitionstart", "d.ontransitionend", "d.ontransitioncancel", "d.oncopy", "d.oncut", "d.onpaste", "d.pointerLockElement", "d.fullscreenElement", "d.pictureInPictureElement", "d.oncontentvisibilityautostatechange", "d.onoverscroll", "d.onscrollend", "d.onbeforematch", "d.onbeforetoggle", "d.ontouchcancel", "d.ontouchend", "d.ontouchmove", "d.ontouchstart", "d.ownerDocument", "d.parentNode", "d.parentElement", "d.previousSibling", "d.nextSibling", "d.nodeValue", "d.textContent"],
    f"https://{domain}": ["origin"],
    "2.0375001430511475": ["devicePixelRatio"],
    "T": ["isSecureContext", "originAgentCluster", "offscreenBuffering", "n.cookieEnabled", "n.onLine", "d.hidden", "d.webkitHidden", "d.fullscreenEnabled", "d.webkitFullscreenEnabled", "d.pictureInPictureEnabled", "d.isConnected"],
    "N": ["alert", "atob", "blur", "btoa", "cancelAnimationFrame", "cancelIdleCallback", "captureEvents", "clearInterval", "clearTimeout", "close", "confirm", "createImageBitmap", "fetch", "find", "focus", "getComputedStyle", "getSelection", "matchMedia", "moveBy", "moveTo", "open", "postMessage", "print", "prompt", "queueMicrotask", "releaseEvents", "reportError", "requestAnimationFrame", "requestIdleCallback", "resizeBy", "resizeTo", "scroll", "scrollBy", "scrollTo", "setInterval", "setTimeout", "stop", "structuredClone", "webkitCancelAnimationFrame", "webkitRequestAnimationFrame", "getComputedAccessibleNode", "openDatabase", "webkitRequestFileSystem", "webkitResolveLocalFileSystemURL", "getDigitalGoodsService", "getLockScreenData", "getScreenDetails", "addEventListener", "dispatchEvent", "removeEventListener", "Object", "Function", "Number", "parseFloat", "parseInt", "Boolean", "String", "Symbol", "Date", "Promise", "RegExp", "Error", "AggregateError", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "ArrayBuffer", "Uint8Array", "Int8Array", "Uint16Array", "Int16Array", "Uint32Array", "Int32Array", "Float32Array", "Float64Array", "Uint8ClampedArray", "BigUint64Array", "BigInt64Array", "DataView", "Map", "BigInt", "Set", "WeakMap", "WeakSet", "Proxy", "FinalizationRegistry", "WeakRef", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "escape", "unescape", "eval", "isFinite", "isNaN", "webkitSpeechRecognitionEvent", "webkitSpeechRecognitionError", "webkitSpeechRecognition", "webkitSpeechGrammarList", "webkitSpeechGrammar", "WebSocketStream", "VisibilityStateEntry", "ViewTransition", "VideoPlaybackQuality", "VTTRegion", "TrackDefaultList", "TrackDefault", "SpeechSynthesisUtterance", "SpeechSynthesisEvent", "SpeechSynthesisErrorEvent", "ViewTimeline", "ScrollTimeline", "RemotePlayback", "PushSubscriptionOptions", "PushSubscription", "PushManager", "Permissions", "PermissionStatus", "PeriodicSyncManager", "PaymentRequestUpdateEvent", "PaymentManager", "OverscrollEvent", "Notification", "NavigatorUAData", "MutationEvent", "MediaSession", "MediaMetadata", "MathMLElement", "MLModelLoader", "ML", "HighlightRegistry", "Highlight", "HTMLSelectMenuElement", "GamepadButtonEvent", "GamepadAxisEvent", "FormattedText", "TextDirective", "SelectorDirective", "Directive", "Ink", "DelegatedInkTrailPresenter", "ContentVisibilityAutoStateChangeEvent", "ContentIndex", "PartRoot", "Part", "NodePart", "DocumentPartRoot", "ChildNodePart", "CanvasFilter", "CSSToggleMap", "CSSToggleEvent", "CSSToggle", "CSSStartingStyleRule", "CSSScopeRule", "CSSTryRule", "CSSPositionFallbackRule", "CSSRGB", "CSSHWB", "CSSHSL", "CSSColorValue", "BluetoothUUID", "BeforeCreatePolicyEvent", "BackgroundFetchRegistration", "BackgroundFetchRecord", "BackgroundFetchManager", "VideoTrackList", "VideoTrack", "AudioTrackList", "AudioTrack", "DocumentTimeline", "CSSTransition", "CSSAnimation", "AnimationTimeline", "AnimationPlaybackEvent", "ComputedAccessibleNode", "AccessibleNodeList", "AccessibleNode", "Option", "Image", "Audio", "webkitURL", "webkitRTCPeerConnection", "webkitMediaStream", "WebKitMutationObserver", "WebKitCSSMatrix", "XSLTProcessor", "XPathResult", "XPathExpression", "XPathEvaluator", "XMLSerializer", "XMLHttpRequestUpload", "XMLHttpRequestEventTarget", "XMLHttpRequest", "XMLDocument", "WritableStreamDefaultWriter", "WritableStreamDefaultController", "WritableStream", "Worker", "Window", "WheelEvent", "WebSocket", "WebGLVertexArrayObject", "WebGLUniformLocation", "WebGLTransformFeedback", "WebGLTexture", "WebGLSync", "WebGLShaderPrecisionFormat", "WebGLShader", "WebGLSampler", "WebGLRenderingContext", "WebGLRenderbuffer", "WebGLQuery", "WebGLProgram", "WebGLFramebuffer", "WebGLContextEvent", "WebGLBuffer", "WebGLActiveInfo", "WebGL2RenderingContext", "WaveShaperNode", "VisualViewport", "VirtualKeyboardGeometryChangeEvent", "ValidityState", "VTTCue", "UserActivation", "URLSearchParams", "URLPattern", "URL", "UIEvent", "TrustedTypePolicyFactory", "TrustedTypePolicy", "TrustedScriptURL", "TrustedScript", "TrustedHTML", "TreeWalker", "TransitionEvent", "TransformStreamDefaultController", "TransformStream", "TrackEvent", "TouchList", "TouchEvent", "Touch", "TimeRanges", "TextTrackList", "TextTrackCueList", "TextTrackCue", "TextTrack", "TextMetrics", "TextEvent", "TextEncoderStream", "TextEncoder", "TextDecoderStream", "TextDecoder", "Text", "TaskSignal", "TaskPriorityChangeEvent", "TaskController", "TaskAttributionTiming", "SyncManager", "SubmitEvent", "StyleSheetList", "StyleSheet", "StylePropertyMapReadOnly", "StylePropertyMap", "StorageEvent", "Storage", "StereoPannerNode", "StaticRange", "SourceBufferList", "SourceBuffer", "ShadowRoot", "Selection", "SecurityPolicyViolationEvent", "ScriptProcessorNode", "ScreenOrientation", "Screen", "Scheduling", "Scheduler", "SVGViewElement", "SVGUseElement", "SVGUnitTypes", "SVGTransformList", "SVGTransform", "SVGTitleElement", "SVGTextPositioningElement", "SVGTextPathElement", "SVGTextElement", "SVGTextContentElement", "SVGTSpanElement", "SVGSymbolElement", "SVGSwitchElement", "SVGStyleElement", "SVGStringList", "SVGStopElement", "SVGSetElement", "SVGScriptElement", "SVGSVGElement", "SVGRectElement", "SVGRect", "SVGRadialGradientElement", "SVGPreserveAspectRatio", "SVGPolylineElement", "SVGPolygonElement", "SVGPointList", "SVGPoint", "SVGPatternElement", "SVGPathElement", "SVGNumberList", "SVGNumber", "SVGMetadataElement", "SVGMatrix", "SVGMaskElement", "SVGMarkerElement", "SVGMPathElement", "SVGLinearGradientElement", "SVGLineElement", "SVGLengthList", "SVGLength", "SVGImageElement", "SVGGraphicsElement", "SVGGradientElement", "SVGGeometryElement", "SVGGElement", "SVGForeignObjectElement", "SVGFilterElement", "SVGFETurbulenceElement", "SVGFETileElement", "SVGFESpotLightElement", "SVGFESpecularLightingElement", "SVGFEPointLightElement", "SVGFEOffsetElement", "SVGFEMorphologyElement", "SVGFEMergeNodeElement", "SVGFEMergeElement", "SVGFEImageElement", "SVGFEGaussianBlurElement", "SVGFEFuncRElement", "SVGFEFuncGElement", "SVGFEFuncBElement", "SVGFEFuncAElement", "SVGFEFloodElement", "SVGFEDropShadowElement", "SVGFEDistantLightElement", "SVGFEDisplacementMapElement", "SVGFEDiffuseLightingElement", "SVGFEConvolveMatrixElement", "SVGFECompositeElement", "SVGFEComponentTransferElement", "SVGFEColorMatrixElement", "SVGFEBlendElement", "SVGEllipseElement", "SVGElement", "SVGDescElement", "SVGDefsElement", "SVGComponentTransferFunctionElement", "SVGClipPathElement", "SVGCircleElement", "SVGAnimationElement", "SVGAnimatedTransformList", "SVGAnimatedString", "SVGAnimatedRect", "SVGAnimatedPreserveAspectRatio", "SVGAnimatedNumberList", "SVGAnimatedNumber", "SVGAnimatedLengthList", "SVGAnimatedLength", "SVGAnimatedInteger", "SVGAnimatedEnumeration", "SVGAnimatedBoolean", "SVGAnimatedAngle", "SVGAnimateTransformElement", "SVGAnimateMotionElement", "SVGAnimateElement", "SVGAngle", "SVGAElement", "Response", "ResizeObserverSize", "ResizeObserverEntry", "ResizeObserver", "Request", "ReportingObserver", "ReadableStreamDefaultReader", "ReadableStreamDefaultController", "ReadableStreamBYOBRequest", "ReadableStreamBYOBReader", "ReadableStream", "ReadableByteStreamController", "Range", "RadioNodeList", "RTCTrackEvent", "RTCStatsReport", "RTCSessionDescription", "RTCSctpTransport", "RTCRtpTransceiver", "RTCRtpSender", "RTCRtpReceiver", "RTCPeerConnectionIceEvent", "RTCPeerConnectionIceErrorEvent", "RTCPeerConnection", "RTCIceTransport", "RTCIceCandidate", "RTCErrorEvent", "RTCError", "RTCEncodedVideoFrame", "RTCEncodedAudioFrame", "RTCDtlsTransport", "RTCDataChannelEvent", "RTCDataChannel", "RTCDTMFToneChangeEvent", "RTCDTMFSender", "RTCCertificate", "PromiseRejectionEvent", "ProgressEvent", "Profiler", "ProcessingInstruction", "PopStateEvent", "PointerEvent", "PluginArray", "Plugin", "PictureInPictureWindow", "PictureInPictureEvent", "PeriodicWave", "PerformanceTiming", "PerformanceServerTiming", "PerformanceResourceTiming", "PerformancePaintTiming", "PerformanceObserverEntryList", "PerformanceObserver", "PerformanceNavigationTiming", "PerformanceNavigation", "PerformanceMeasure", "PerformanceMark", "PerformanceLongTaskTiming", "PerformanceEventTiming", "PerformanceEntry", "PerformanceElementTiming", "Performance", "Path2D", "PannerNode", "PageTransitionEvent", "OverconstrainedError", "OscillatorNode", "OffscreenCanvasRenderingContext2D", "OffscreenCanvas", "OfflineAudioContext", "OfflineAudioCompletionEvent", "NodeList", "NodeIterator", "NodeFilter", "Node", "NetworkInformation", "Navigator", "NavigationTransition", "NavigationHistoryEntry", "NavigationDestination", "NavigationCurrentEntryChangeEvent", "Navigation", "NavigateEvent", "NamedNodeMap", "MutationRecord", "MutationObserver", "MouseEvent", "MimeTypeArray", "MimeType", "MessagePort", "MessageEvent", "MessageChannel", "MediaStreamTrackProcessor", "MediaStreamTrackGenerator", "MediaStreamTrackEvent", "MediaStreamTrack", "MediaStreamEvent", "MediaStreamAudioSourceNode", "MediaStreamAudioDestinationNode", "MediaStream", "MediaSourceHandle", "MediaSource", "MediaRecorder", "MediaQueryListEvent", "MediaQueryList", "MediaList", "MediaError", "MediaEncryptedEvent", "MediaElementAudioSourceNode", "MediaCapabilities", "Location", "LayoutShiftAttribution", "LayoutShift", "LargestContentfulPaint", "KeyframeEffect", "KeyboardEvent", "IntersectionObserverEntry", "IntersectionObserver", "InputEvent", "InputDeviceInfo", "InputDeviceCapabilities", "ImageData", "ImageCapture", "ImageBitmapRenderingContext", "ImageBitmap", "IdleDeadline", "IIRFilterNode", "IDBVersionChangeEvent", "IDBTransaction", "IDBRequest", "IDBOpenDBRequest", "IDBObjectStore", "IDBKeyRange", "IDBIndex", "IDBFactory", "IDBDatabase", "IDBCursorWithValue", "IDBCursor", "History", "Headers", "HashChangeEvent", "HTMLVideoElement", "HTMLUnknownElement", "HTMLUListElement", "HTMLTrackElement", "HTMLTitleElement", "HTMLTimeElement", "HTMLTextAreaElement", "HTMLTemplateElement", "HTMLTableSectionElement", "HTMLTableRowElement", "HTMLTableElement", "HTMLTableColElement", "HTMLTableCellElement", "HTMLTableCaptionElement", "HTMLStyleElement", "HTMLSpanElement", "HTMLSourceElement", "HTMLSlotElement", "HTMLSelectElement", "HTMLScriptElement", "HTMLQuoteElement", "HTMLProgressElement", "HTMLPreElement", "HTMLPictureElement", "HTMLParamElement", "HTMLParagraphElement", "HTMLOutputElement", "HTMLOptionsCollection", "HTMLOptionElement", "HTMLOptGroupElement", "HTMLObjectElement", "HTMLOListElement", "HTMLModElement", "HTMLMeterElement", "HTMLMetaElement", "HTMLMenuElement", "HTMLMediaElement", "HTMLMarqueeElement", "HTMLMapElement", "HTMLLinkElement", "HTMLLegendElement", "HTMLLabelElement", "HTMLLIElement", "HTMLInputElement", "HTMLImageElement", "HTMLIFrameElement", "HTMLHtmlElement", "HTMLHeadingElement", "HTMLHeadElement", "HTMLHRElement", "HTMLFrameSetElement", "HTMLFrameElement", "HTMLFormElement", "HTMLFormControlsCollection", "HTMLFontElement", "HTMLFieldSetElement", "HTMLEmbedElement", "HTMLElement", "HTMLDocument", "HTMLDivElement", "HTMLDirectoryElement", "HTMLDialogElement", "HTMLDetailsElement", "HTMLDataListElement", "HTMLDataElement", "HTMLDListElement", "HTMLCollection", "HTMLCanvasElement", "HTMLButtonElement", "HTMLBodyElement", "HTMLBaseElement", "HTMLBRElement", "HTMLAudioElement", "HTMLAreaElement", "HTMLAnchorElement", "HTMLAllCollection", "GeolocationPositionError", "GeolocationPosition", "GeolocationCoordinates", "Geolocation", "GamepadHapticActuator", "GamepadEvent", "GamepadButton", "Gamepad", "GainNode", "FormDataEvent", "FormData", "FontFaceSetLoadEvent", "FontFace", "FocusEvent", "FileReader", "FileList", "File", "FeaturePolicy", "External", "EventTarget", "EventSource", "EventCounts", "Event", "ErrorEvent", "ElementInternals", "Element", "DynamicsCompressorNode", "DragEvent", "DocumentType", "DocumentFragment", "Document", "DelayNode", "DecompressionStream", "DataTransferItemList", "DataTransferItem", "DataTransfer", "DOMTokenList", "DOMStringMap", "DOMStringList", "DOMRectReadOnly", "DOMRectList", "DOMRect", "DOMQuad", "DOMPointReadOnly", "DOMPoint", "DOMParser", "DOMMatrixReadOnly", "DOMMatrix", "DOMImplementation", "DOMException", "DOMError", "CustomStateSet", "CustomEvent", "CustomElementRegistry", "Crypto", "CountQueuingStrategy", "ConvolverNode", "ConstantSourceNode", "CompressionStream", "CompositionEvent", "Comment", "CloseEvent", "ClipboardEvent", "CharacterData", "ChannelSplitterNode", "ChannelMergerNode", "CanvasRenderingContext2D", "CanvasPattern", "CanvasGradient", "CanvasCaptureMediaStreamTrack", "CSSVariableReferenceValue", "CSSUnparsedValue", "CSSUnitValue", "CSSTranslate", "CSSTransformValue", "CSSTransformComponent", "CSSSupportsRule", "CSSStyleValue", "CSSStyleSheet", "CSSStyleRule", "CSSStyleDeclaration", "CSSSkewY", "CSSSkewX", "CSSSkew", "CSSScale", "CSSRuleList", "CSSRule", "CSSRotate", "CSSPropertyRule", "CSSPositionValue", "CSSPerspective", "CSSPageRule", "CSSNumericValue", "CSSNumericArray", "CSSNamespaceRule", "CSSMediaRule", "CSSMatrixComponent", "CSSMathValue", "CSSMathSum", "CSSMathProduct", "CSSMathNegate", "CSSMathMin", "CSSMathMax", "CSSMathInvert", "CSSMathClamp", "CSSLayerStatementRule", "CSSLayerBlockRule", "CSSKeywordValue", "CSSKeyframesRule", "CSSKeyframeRule", "CSSImportRule", "CSSImageValue", "CSSGroupingRule", "CSSFontPaletteValuesRule", "CSSFontFaceRule", "CSSCounterStyleRule", "CSSContainerRule", "CSSConditionRule", "CDATASection", "ByteLengthQueuingStrategy", "BroadcastChannel", "BlobEvent", "Blob", "BiquadFilterNode", "BeforeUnloadEvent", "BeforeInstallPromptEvent", "BaseAudioContext", "BarProp", "AudioWorkletNode", "AudioSinkInfo", "AudioScheduledSourceNode", "AudioProcessingEvent", "AudioParamMap", "AudioParam", "AudioNode", "AudioListener", "AudioDestinationNode", "AudioContext", "AudioBufferSourceNode", "AudioBuffer", "Attr", "AnimationEvent", "AnimationEffect", "Animation", "AnalyserNode", "AbstractRange", "AbortSignal", "AbortController", "Iterator", "AbsoluteOrientationSensor", "Accelerometer", "AudioWorklet", "BatteryManager", "Cache", "CacheStorage", "Clipboard", "ClipboardItem", "CookieChangeEvent", "CookieStore", "CookieStoreManager", "Credential", "CredentialsContainer", "CryptoKey", "DeviceMotionEvent", "DeviceMotionEventAcceleration", "DeviceMotionEventRotationRate", "DeviceOrientationEvent", "FederatedCredential", "GravitySensor", "Gyroscope", "Keyboard", "KeyboardLayoutMap", "LinearAccelerationSensor", "Lock", "LockManager", "MIDIAccess", "MIDIConnectionEvent", "MIDIInput", "MIDIInputMap", "MIDIMessageEvent", "MIDIOutput", "MIDIOutputMap", "MIDIPort", "MediaDeviceInfo", "MediaDevices", "MediaKeyMessageEvent", "MediaKeySession", "MediaKeyStatusMap", "MediaKeySystemAccess", "MediaKeys", "NavigationPreloadManager", "NavigatorManagedData", "OrientationSensor", "PasswordCredential", "RelativeOrientationSensor", "Sanitizer", "ScreenDetailed", "ScreenDetails", "Sensor", "SensorErrorEvent", "ServiceWorker", "ServiceWorkerContainer", "ServiceWorkerRegistration", "StorageManager", "SubtleCrypto", "VirtualKeyboard", "WebTransport", "WebTransportBidirectionalStream", "WebTransportDatagramDuplexStream", "WebTransportError", "Worklet", "XRDOMOverlayState", "XRLayer", "XRWebGLBinding", "AmbientLightSensor", "Magnetometer", "AudioData", "EncodedAudioChunk", "EncodedVideoChunk", "ImageTrack", "ImageTrackList", "VideoColorSpace", "VideoFrame", "AudioDecoder", "AudioEncoder", "ImageDecoder", "VideoDecoder", "VideoEncoder", "AuthenticatorAssertionResponse", "AuthenticatorAttestationResponse", "AuthenticatorResponse", "PublicKeyCredential", "BackForwardCacheRestoration", "BarcodeDetector", "Bluetooth", "BluetoothCharacteristicProperties", "BluetoothDevice", "BluetoothRemoteGATTCharacteristic", "BluetoothRemoteGATTDescriptor", "BluetoothRemoteGATTServer", "BluetoothRemoteGATTService", "BluetoothAdvertisingEvent", "BluetoothLEScan", "BluetoothManufacturerDataMap", "BluetoothServiceDataMap", "CharacterBoundsUpdateEvent", "EditContext", "TextFormat", "TextFormatUpdateEvent", "TextUpdateEvent", "ContactAddress", "ContactsManager", "DevicePosture", "FaceDetector", "FileSystemDirectoryHandle", "FileSystemFileHandle", "FileSystemHandle", "FileSystemWritableFileStream", "FragmentDirective", "GPU", "GPUAdapter", "GPUAdapterInfo", "GPUBindGroup", "GPUBindGroupLayout", "GPUBuffer", "GPUCanvasContext", "GPUCommandBuffer", "GPUCommandEncoder", "GPUCompilationInfo", "GPUCompilationMessage", "GPUComputePassEncoder", "GPUComputePipeline", "GPUDevice", "GPUDeviceLostInfo", "GPUError", "GPUExternalTexture", "GPUInternalError", "GPUOutOfMemoryError", "GPUPipelineError", "GPUPipelineLayout", "GPUQuerySet", "GPUQueue", "GPURenderBundle", "GPURenderBundleEncoder", "GPURenderPassEncoder", "GPURenderPipeline", "GPUSampler", "GPUShaderModule", "GPUSupportedFeatures", "GPUSupportedLimits", "GPUTexture", "GPUTextureView", "GPUUncapturedErrorEvent", "GPUValidationError", "WGSLLanguageFeatures", "GamepadTouch", "HandwritingStroke", "IdentityCredential", "IdentityProvider", "IdleDetector", "LaunchParams", "LaunchQueue", "MLContext", "MerchantValidationEvent", "NDEFMessage", "NDEFReader", "NDEFReadingEvent", "NDEFRecord", "OTPCredential", "PaymentAddress", "PaymentRequest", "PaymentResponse", "PaymentMethodChangeEvent", "PerformanceLongAnimationFrameTiming", "PerformanceScriptTiming", "Presentation", "PresentationAvailability", "PresentationConnection", "PresentationConnectionAvailableEvent", "PresentationConnectionCloseEvent", "PresentationConnectionList", "PresentationReceiver", "PresentationRequest", "PressureObserver", "PressureRecord", "PrivateAttribution", "SoftNavigationEntry", "StorageBucket", "StorageBucketManager", "TextDetector", "TimestampTrigger", "ToggleEvent", "USB", "USBAlternateInterface", "USBConfiguration", "USBConnectionEvent", "USBDevice", "USBEndpoint", "USBInTransferResult", "USBInterface", "USBIsochronousInTransferPacket", "USBIsochronousInTransferResult", "USBIsochronousOutTransferPacket", "USBIsochronousOutTransferResult", "USBOutTransferResult", "WakeLock", "WakeLockSentinel", "XRAnchor", "XRAnchorSet", "XRBoundedReferenceSpace", "XRCPUDepthInformation", "XRCamera", "XRDepthInformation", "XRFrame", "XRHitTestResult", "XRHitTestSource", "XRInputSource", "XRInputSourceArray", "XRInputSourceEvent", "XRInputSourcesChangeEvent", "XRLightEstimate", "XRLightProbe", "XRPose", "XRRay", "XRReferenceSpace", "XRReferenceSpaceEvent", "XRRenderState", "XRRigidTransform", "XRSession", "XRSessionEvent", "XRSpace", "XRSystem", "XRTransientInputHitTestResult", "XRTransientInputHitTestSource", "XRView", "XRViewerPose", "XRViewport", "XRWebGLDepthInformation", "XRWebGLLayer", "XRCompositionLayer", "XRProjectionLayer", "XRSubImage", "XRWebGLSubImage", "XRHand", "XRJointPose", "XRJointSpace", "XRImageTrackingResult", "XRPlane", "XRPlaneSet", "n.getGamepads", "n.javaEnabled", "n.sendBeacon", "n.vibrate", "n.canShare", "n.share", "n.clearAppBadge", "n.getBattery", "n.getUserMedia", "n.requestMIDIAccess", "n.requestMediaKeySystemAccess", "n.setAppBadge", "n.webkitGetUserMedia", "n.createHandwritingRecognizer", "n.queryHandwritingRecognizer", "n.getEnvironmentIntegrity", "n.getInstalledRelatedApps", "d.adoptNode", "d.append", "d.captureEvents", "d.caretRangeFromPoint", "d.clear", "d.close", "d.createAttribute", "d.createAttributeNS", "d.createCDATASection", "d.createComment", "d.createDocumentFragment", "d.createElement", "d.createElementNS", "d.createEvent", "d.createExpression", "d.createNSResolver", "d.createNodeIterator", "d.createProcessingInstruction", "d.createRange", "d.createTextNode", "d.createTreeWalker", "d.elementFromPoint", "d.elementsFromPoint", "d.evaluate", "d.execCommand", "d.exitFullscreen", "d.exitPictureInPicture", "d.exitPointerLock", "d.getElementById", "d.getElementsByClassName", "d.getElementsByName", "d.getElementsByTagName", "d.getElementsByTagNameNS", "d.getSelection", "d.hasFocus", "d.importNode", "d.open", "d.prepend", "d.queryCommandEnabled", "d.queryCommandIndeterm", "d.queryCommandState", "d.queryCommandSupported", "d.queryCommandValue", "d.querySelector", "d.querySelectorAll", "d.releaseEvents", "d.replaceChildren", "d.webkitCancelFullScreen", "d.webkitExitFullscreen", "d.write", "d.writeln", "d.getAnimations", "d.getPartRoot", "d.hasStorageAccess", "d.requestStorageAccess", "d.startViewTransition", "d.hasPrivateToken", "d.hasRedemptionRecord", "d.appendChild", "d.cloneNode", "d.compareDocumentPosition", "d.contains", "d.getRootNode", "d.hasChildNodes", "d.insertBefore", "d.isDefaultNamespace", "d.isEqualNode", "d.isSameNode", "d.lookupNamespaceURI", "d.lookupPrefix", "d.normalize", "d.removeChild", "d.replaceChild", "d.addEventListener", "d.dispatchEvent", "d.removeEventListener"],
    "C": ["Array"],
    "Infinity": ["Infinity"],
    "NaN": ["NaN"],
    "u": ["undefined", "event"],
    "Google Inc.": ["n.vendor"],
    "Mozilla": ["n.appCodeName"],
    "Netscape": ["n.appName"],
    useragent.lstrip('Mozilla/'): ["n.appVersion"],
    "Linux armv81": ["n.platform"],
    "Gecko": ["n.product"],
    useragent: ["n.userAgent"],
    "es-CO": ["n.language"],
    "es-CO,es-US,es-419,es": ["n.languages"],
    "about:blank": ["d.URL", "d.documentURI", "d.referrer"],
    "BackCompat": ["d.compatMode"],
    "UTF-8": ["d.characterSet", "d.charset", "d.inputEncoding"],
    "text/html": ["d.contentType"],
    domain: ["d.domain"],
    "s": ["d.cookie"],
    datetime.now().strftime("%m/%d/%Y %H:%M:%S"): ["d.lastModified"],
    "complete": ["d.readyState"],
    "off": ["d.designMode"],
    "hidden": ["d.visibilityState", "d.webkitVisibilityState"],
    "": ["d.adoptedStyleSheets"],
    "#document": ["d.nodeName"],
    f"https://{domain}": ["d.baseURI"]
}
