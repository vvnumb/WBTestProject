import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict

from config.registry import Registry


class SelfImplementedHTTPServer(BaseHTTPRequestHandler):
	# url: query_params, service
	_get_endpoints = {
		"/items": (("id",), Registry.get_single_item_service()),
		"/items/list": ((), Registry.get_list_item_service()),
	}
	
	# url: query_params, body_params, service
	_post_endpoints = {
		"/items": ((), {"value": int}, Registry.save_item_service())
	}
	
	def do_GET(self):
		
		query_params = self._parse_params()
		if self.path not in self._get_endpoints:
			self._raise_exception(404)
			return
		params = {}
		endpoint_params, service = self._get_endpoints.get(self.path, ([], lambda *args: {}))
		for endpoint_param in endpoint_params:
			if endpoint_param not in query_params:
				self._raise_exception(400)
				return
			try:
				query_param = int(query_params[endpoint_param])
			except ValueError:
				query_param = query_params[endpoint_param]
			
			params[endpoint_param] = query_param
		self._respond(service(**params))
	
	def do_POST(self):
		# todo: повторение, dry
		body_payload = self._get_body_payload()
		query_params = self._parse_params()
		if self.path not in self._post_endpoints:
			self._raise_exception(404)
			return
		params = {}
		endpoint_params, required_payload, service = self._post_endpoints.get(
			self.path, ([], {}, lambda *args: {})
		)
		for endpoint_param in endpoint_params:
			if endpoint_param not in query_params:
				self._raise_exception(400)
				return
			try:
				query_param = int(query_params[endpoint_param])
			except ValueError:
				query_param = query_params[endpoint_param]
			
			params[endpoint_param] = query_param
		
		for body_param, param_type in required_payload.items():
			if body_param not in body_payload:
				self._raise_exception(400)
				return
			params[body_param] = param_type(body_payload[body_param][0])
		
		self._respond(service(**params))
	
	def _parse_params(self) -> Dict[str, Any]:
		params = {}
		try:
			i = self.path.index("?") + 1
			params = dict([tuple(p.split("=")) for p in self.path[i:].split("&")])
			self.path = self.path[:i - 1]
		except ValueError:
			pass  # нет квери параметров
		
		return params
	
	def _get_body_payload(self) -> Dict[str, Any]:
		ctype, pdict = cgi.parse_header(self.headers['content-type'])
		pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
		multipart_data = cgi.parse_multipart(self.rfile, pdict)
		return multipart_data
	
	def _raise_exception(self, status):
		self.send_response(status)
		self.send_header("Content-type", "application/json")
		self.end_headers()
	
	def _respond(self, data: dict):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write(
			bytes(json.dumps(data), "utf-8")
		)


if __name__ == "__main__":
	
	webServer = HTTPServer(("localhost", 8080), MyServer)
	print("Server started http://%s:%s" % ("localhost", 8080))
	
	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass
	
	webServer.server_close()
	print("Server stopped.")
