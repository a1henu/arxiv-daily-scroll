---
layout: default
title: Multimodal Real-Time Anomaly Detection and Industrial Applications
---

# Multimodal Real-Time Anomaly Detection and Industrial Applications
**arXiv**：[2511.18698v1](https://arxiv.org/abs/2511.18698) · [PDF](https://arxiv.org/pdf/2511.18698.pdf)  
**作者**：Aman Verma, Keshav Samdani, Mohd. Samiuddin Shafi  

**一句话要点**：提出多模态实时异常检测系统，用于工业安全与通用监控场景。

**关键词**：多模态异常检测, 实时视频处理, 音频识别, 工业安全监控, 跨模态融合

## 3 点简述
- 核心问题：实时多模态活动识别与异常检测在工业应用中的准确性和鲁棒性需求。
- 方法要点：集成视频和音频处理，采用双向跨模态注意力和多模型融合提升性能。
- 实验或效果：在标准硬件上实现高精度实时检测，适用于工业安全场景。

## 摘要（原文）

> This paper presents the design, implementation, and evolution of a comprehensive multimodal room-monitoring system that integrates synchronized video and audio processing for real-time activity recognition and anomaly detection. We describe two iterations of the system: an initial lightweight implementation using YOLOv8, ByteTrack, and the Audio Spectrogram Transformer (AST), and an advanced version that incorporates multi-model audio ensembles, hybrid object detection, bidirectional cross-modal attention, and multi-method anomaly detection. The evolution demonstrates significant improvements in accuracy, robustness, and industrial applicability. The advanced system combines three audio models (AST, Wav2Vec2, and HuBERT) for comprehensive audio understanding, dual object detectors (YOLO and DETR) for improved accuracy, and sophisticated fusion mechanisms for enhanced cross-modal learning. Experimental evaluation shows the system's effectiveness in general monitoring scenarios as well as specialized industrial safety applications, achieving real-time performance on standard hardware while maintaining high accuracy.

