---
layout: default
title: HelixTrack: Event-Based Tracking and RPM Estimation of Propeller-like Objects
---

# HelixTrack: Event-Based Tracking and RPM Estimation of Propeller-like Objects
**arXiv**：[2603.09235v1](https://arxiv.org/abs/2603.09235) · [PDF](https://arxiv.org/pdf/2603.09235.pdf)  
**作者**：Radim Spetlik, Michal Pliska, Vojtěch Vrba, Jiri Matas  

**一句话要点**：提出HelixTrack方法，以解决无人机和旋转机械中螺旋桨类物体在强干扰下的微秒级跟踪与转速估计问题。

**关键词**：事件相机跟踪, 螺旋桨转速估计, 微秒级感知, 卡尔曼滤波, 单应性变换, 无人机安全

## 3 点简述
- 核心问题：帧基和事件基跟踪器在螺旋桨周期性运动下因违反平滑假设而漂移或失效。
- 方法要点：通过实时估计单应性将事件从图像平面反投影到转子平面，结合卡尔曼滤波和批量迭代更新联合跟踪与估计转速。
- 实验或效果：在自建TQE数据集上，HelixTrack以约11.8倍实时速度处理事件，微秒级延迟，性能优于基线方法。

## 摘要（原文）

> Safety-critical perception for unmanned aerial vehicles and rotating machinery requires microsecond-latency tracking of fast, periodic motion under egomotion and strong distractors. Frame-based and event-based trackers drift or break on propellers because periodic signatures violate their smooth-motion assumptions. We tackle this gap with HelixTrack, a fully event-driven method that jointly tracks propeller-like objects and estimates their rotations per minute (RPM). Incoming events are back-warped from the image plane into the rotor plane via a homography estimated on the fly. A Kalman Filter maintains instantaneous estimates of phase. Batched iterative updates refine the object pose by coupling phase residuals to geometry. To our knowledge, no public dataset targets joint tracking and RPM estimation of propeller-like objects. We therefore introduce the Timestamped Quadcopter with Egomotion (TQE) dataset with 13 high-resolution event sequences, containing 52 rotating objects in total, captured at distances of 2 m / 4 m, with increasing egomotion and microsecond RPM ground truth. On TQE, HelixTrack processes full-rate events (approx. 11.8x real time) faster than real time and microsecond latency. It consistently outperforms per-event and aggregation-based baselines adapted for RPM estimation.

