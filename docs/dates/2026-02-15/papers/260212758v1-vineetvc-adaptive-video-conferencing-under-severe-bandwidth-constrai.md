---
layout: default
title: VineetVC: Adaptive Video Conferencing Under Severe Bandwidth Constraints Using Audio-Driven Talking-Head Reconstruction
---

# VineetVC: Adaptive Video Conferencing Under Severe Bandwidth Constraints Using Audio-Driven Talking-Head Reconstruction
**arXiv**：[2602.12758v1](https://arxiv.org/abs/2602.12758) · [PDF](https://arxiv.org/pdf/2602.12758.pdf)  
**作者**：Vineet Kumar Rakesh, Soumya Mazumdar, Tapas Samanta, Hemendra Kumar Pandey, Amitabha Das, Sarbajit Pal  

**一句话要点**：提出VineetVC系统，在严重带宽限制下通过音频驱动头部重建自适应视频会议

**关键词**：视频会议, 带宽自适应, 音频驱动重建, WebRTC, 头部合成

## 3 点简述
- 核心问题：带宽耗尽导致视频会议质量下降，如丢包增加和延迟显著上升
- 方法要点：集成WebRTC与音频驱动头部重建路径，支持带宽模式切换和客户端状态记录
- 实验或效果：合成流中位带宽为32.80 kbps，可替代摄像头轨道提升稳定性

## 摘要（原文）

> Intense bandwidth depletion within consumer and constrained networks has the potential to undermine the stability of real-time video conferencing: encoder rate management becomes saturated, packet loss escalates, frame rates deteriorate, and end-to-end latency significantly increases. This work delineates an adaptive conferencing system that integrates WebRTC media delivery with a supplementary audio-driven talking-head reconstruction pathway and telemetry-driven mode regulation. The system consists of a WebSocket signaling service, an optional SFU for multi-party transmission, a browser client capable of real-time WebRTC statistics extraction and CSV telemetry export, and an AI REST service that processes a reference face image and recorded audio to produce a synthesized MP4; the browser can substitute its outbound camera track with the synthesized stream with a median bandwidth of 32.80 kbps. The solution incorporates a bandwidth-mode switching strategy and a client-side mode-state logger.

