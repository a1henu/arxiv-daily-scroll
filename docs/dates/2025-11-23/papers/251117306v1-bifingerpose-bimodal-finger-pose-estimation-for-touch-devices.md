---
layout: default
title: BiFingerPose: Bimodal Finger Pose Estimation for Touch Devices
---

# BiFingerPose: Bimodal Finger Pose Estimation for Touch Devices
**arXiv**：[2511.17306v1](https://arxiv.org/abs/2511.17306) · [PDF](https://arxiv.org/pdf/2511.17306.pdf)  
**作者**：Xiongjun Guan, Zhiyu Pan, Jianjiang Feng, Jie Zhou  

**一句话要点**：提出BiFingerPose以解决触摸设备上手指姿态估计的精度和角度限制问题

**关键词**：手指姿态估计, 双模态融合, 触摸设备交互, 电容图像, 指纹传感器, 人机交互

## 3 点简述
- 现有电容图像方法估计手指姿态时，限于俯仰和偏航角，大角度输入精度下降
- 采用双模态输入，结合电容图像和指纹补丁，可靠估计滚转角并提升其他参数性能
- 用户研究显示，预测性能提升超21%，任务完成效率提高2.5倍，操作准确率提升23%

## 摘要（原文）

> Finger pose offers promising opportunities to expand human computer interaction capability of touchscreen devices. Existing finger pose estimation algorithms that can be implemented in portable devices predominantly rely on capacitive images, which are currently limited to estimating pitch and yaw angles and exhibit reduced accuracy when processing large-angle inputs (especially when it is greater than 45 degrees). In this paper, we propose BiFingerPose, a novel bimodal based finger pose estimation algorithm capable of simultaneously and accurately predicting comprehensive finger pose information. A bimodal input is explored, including a capacitive image and a fingerprint patch obtained from the touchscreen with an under-screen fingerprint sensor. Our approach leads to reliable estimation of roll angle, which is not achievable using only a single modality. In addition, the prediction performance of other pose parameters has also been greatly improved. The evaluation of a 12-person user study on continuous and discrete interaction tasks further validated the advantages of our approach. Specifically, BiFingerPose outperforms previous SOTA methods with over 21% improvement in prediction performance, 2.5 times higher task completion efficiency, and 23% better user operation accuracy, demonstrating its practical superiority. Finally, we delineate the application space of finger pose with respect to enhancing authentication security and improving interactive experiences, and develop corresponding prototypes to showcase the interaction potential. Our code will be available at https://github.com/XiongjunGuan/DualFingerPose.

