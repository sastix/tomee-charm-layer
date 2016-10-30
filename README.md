## Overview

Apache TomEE, pronounced "Tommy", is an all-Apache Java EE 6 Web Profile
certified application server extends Apache Tomcat.
Apache TomEE is assembled from a vanilla Apache Tomcat zip file.

Features:

 * Java Servlets	￼	￼	￼	￼	￼
 * Java ServerPages (JSP)	￼	￼	￼	￼	￼
 * Java ServerFaces (JSF)		￼	￼	￼	￼
 * Java Transaction API (JTA)		￼	￼	￼	￼	￼
 * Java Persistence API (JPA)		￼	￼	￼	￼	￼
 * Java Contexts and Dependency Injection (CDI)		￼	￼	￼	￼	￼
 * Java Authentication and Authorization Service (JAAS)		￼	￼	￼	￼	￼
 * Java Authorization Contract for Containers (JACC)		￼	￼	￼	￼	￼
 * JavaMail API		￼	￼	￼	￼	￼
 * Bean Validation		￼	￼	￼	￼	￼
 * Enterprise JavaBeans		￼	￼	￼	￼	￼
 * Java API for RESTful Web Services (JAX-RS)			￼	￼	￼	￼
 * Java API for XML Web Services (JAX-WS)				￼	￼	￼
 * Java EE Connector Architecture				￼	￼	￼
 * Java Messaging Service (JMS)				￼	￼	￼
 * EclipseLink					￼
 * Mojarra


## Usage

To deploy TomEE using this charm you have to do a:

    juju deploy cs:~kos.tsakalozos/apache-tomee

Then you can expose the service:

    juju expose apache-tomee

You can then use `juju status` to get address for the service and then open
it in your web browser with `http://<charm_ip>:8080/`


## Contact Information

- kos.tsakalozos@canonical.com


## Resources

- [Apache TomEE](http://tomee.apache.org/index.html) home page
