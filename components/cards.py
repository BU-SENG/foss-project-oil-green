# components/cards.py
import streamlit as st

def metric_card(title, value, delta=None):
    st.markdown(f"""
    <div class="metric-card">
      <div class="metric-title">{title}</div>
      <div class="metric-value">{value}</div>
      <div class="metric-delta">{delta or ''}</div>
    </div>
    """, unsafe_allow_html=True)

def resource_card(resource):
    st.markdown(f"""
    <div class="resource-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="font-weight:700">{resource.get('title')}</div>
        <div style="font-size:12px; color:#6b7280">{resource.get('category')}</div>
      </div>
      <div style="margin-top:6px; color:#374151">{resource.get('description')}</div>
      <div style="margin-top:8px"><a href="{resource.get('download_url', '#')}">Download</a></div>
    </div>
    """, unsafe_allow_html=True)

def contact_card(contact):
    st.markdown(f"""
    <div class="card">
      <div style="font-weight:700">{contact.get('name')}</div>
      <div style="color:#6b7280">{contact.get('role')} — {contact.get('department')}</div>
      <div style="margin-top:6px">Phone: {contact.get('phone')} • <a href="mailto:{contact.get('email')}">Email</a></div>
    </div>
    """, unsafe_allow_html=True)
