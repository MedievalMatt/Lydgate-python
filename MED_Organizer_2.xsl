<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:strip-space elements="*"/>
    
    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="HEADWORDS">
        <xsl:element name="ROOT">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="HI"/>
    
    <xsl:template match="ORIG"/>
    
    <xsl:template match="ENTRY">
        <xsl:element name="item">
            <xsl:attribute name="id">
                <xsl:value-of select="substring-after(@ID,'MED')"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="FORM">
        <xsl:apply-templates select="*"/>
    </xsl:template>
    
    <xsl:template match="HDORTH">
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="ORTH">
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="REG">
        <xsl:choose>
            <xsl:when test="../name() = 'HDORTH'">
                <xsl:element name="headword">
                    <xsl:apply-templates/>
                </xsl:element>
            </xsl:when>
            <xsl:when test="../name() = 'ORTH'">
                <xsl:element name="variant">
                    <xsl:apply-templates/>
                </xsl:element>
            </xsl:when>
            <xsl:otherwise/>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="POS">
        <xsl:apply-templates select="PS"/>
    </xsl:template>
    
    <xsl:template match="PS">
        <xsl:element name="speech_part">
            <xsl:value-of select="@EXPAN"/>
        </xsl:element>
    </xsl:template>
    
</xsl:stylesheet>