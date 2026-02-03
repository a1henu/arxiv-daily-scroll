---
layout: default
title: Real-Time 2D LiDAR Object Detection Using Three-Frame RGB Scan Encoding
---

# Real-Time 2D LiDAR Object Detection Using Three-Frame RGB Scan Encoding
**arXiv**：[2602.02167v1](https://arxiv.org/abs/2602.02167) · [PDF](https://arxiv.org/pdf/2602.02167.pdf)  
**作者**：Soheil Behnam Roudsari, Alexandre S. Brandão, Felipe N. Martins  

**一句话要点**：提出三帧RGB扫描编码方法，实现嵌入式室内机器人实时2D LiDAR物体检测。

**关键词**：2D LiDAR检测, 时序编码, 嵌入式机器人, 实时处理, YOLOv8, 室内场景

## 3 点简述
- 核心问题：室内服务机器人需隐私友好、嵌入式硬件可行的感知方案，避免RGB视频。
- 方法要点：将连续三帧LiDAR扫描堆叠为RGB通道，作为YOLOv8n输入，保留角度结构和运动线索。
- 实验或效果：在Webots模拟中，mAP@0.5达98.4%，Raspberry Pi 5上实时运行，端到端延迟47.8ms。

## 摘要（原文）

> Indoor service robots need perception that is robust, more privacy-friendly than RGB video, and feasible on embedded hardware. We present a camera-free 2D LiDAR object detection pipeline that encodes short-term temporal context by stacking three consecutive scans as RGB channels, yielding a compact YOLOv8n input without occupancy-grid construction while preserving angular structure and motion cues. Evaluated in Webots across 160 randomized indoor scenarios with strict scenario-level holdout, the method achieves 98.4% mAP@0.5 (0.778 mAP@0.5:0.95) with 94.9% precision and 94.7% recall on four object classes. On a Raspberry Pi 5, it runs in real time with a mean post-warm-up end-to-end latency of 47.8ms per frame, including scan encoding and postprocessing. Relative to a closely related occupancy-grid LiDAR-YOLO pipeline reported on the same platform, the proposed representation is associated with substantially lower reported end-to-end latency. Although results are simulation-based, they suggest that lightweight temporal encoding can enable accurate and real-time LiDAR-only detection for embedded indoor robotics without capturing RGB appearance.

