---
layout: default
title: XAttn-BMD: Multimodal Deep Learning with Cross-Attention for Femoral Neck Bone Mineral Density Estimation
---

# XAttn-BMD: Multimodal Deep Learning with Cross-Attention for Femoral Neck Bone Mineral Density Estimation
**arXiv**：[2511.14604v1](https://arxiv.org/abs/2511.14604) · [PDF](https://arxiv.org/pdf/2511.14604.pdf)  
**作者**：Yilin Zhang, Leo D. Westbury, Elaine M. Dennison, Nicholas C. Harvey, Nicholas R. Fuggle, Rahman Attar  

**一句话要点**：提出XAttn-BMD多模态深度学习框架，通过交叉注意力机制从髋部X光和临床元数据估计股骨颈骨密度。

**关键词**：多模态深度学习, 交叉注意力机制, 骨密度估计, 医学影像分析, 加权损失函数, 临床元数据融合

## 3 点简述
- 核心问题：骨密度低增加骨折风险，需从多模态数据准确估计股骨颈骨密度。
- 方法要点：使用双向交叉注意力机制动态融合图像和元数据特征，并采用加权平滑L1损失处理数据不平衡。
- 实验效果：在Hertfordshire队列数据上，模型优于基线，MSE降低16.7%，MAE降低6.03%，R2分数提高16.4%。

## 摘要（原文）

> Poor bone health is a significant public health concern, and low bone mineral density (BMD) leads to an increased fracture risk, a key feature of osteoporosis. We present XAttn-BMD (Cross-Attention BMD), a multimodal deep learning framework that predicts femoral neck BMD from hip X-ray images and structured clinical metadata. It utilizes a novel bidirectional cross-attention mechanism to dynamically integrate image and metadata features for cross-modal mutual reinforcement. A Weighted Smooth L1 loss is tailored to address BMD imbalance and prioritize clinically significant cases. Extensive experiments on the data from the Hertfordshire Cohort Study show that our model outperforms the baseline models in regression generalization and robustness. Ablation studies confirm the effectiveness of both cross-attention fusion and the customized loss function. Experimental results show that the integration of multimodal data via cross-attention outperforms naive feature concatenation without cross-attention, reducing MSE by 16.7%, MAE by 6.03%, and increasing the R2 score by 16.4%, highlighting the effectiveness of the approach for femoral neck BMD estimation. Furthermore, screening performance was evaluated using binary classification at clinically relevant femoral neck BMD thresholds, demonstrating the model's potential in real-world scenarios.

