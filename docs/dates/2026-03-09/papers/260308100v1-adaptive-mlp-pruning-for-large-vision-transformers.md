---
layout: default
title: Adaptive MLP Pruning for Large Vision Transformers
---

# Adaptive MLP Pruning for Large Vision Transformers
**arXiv**：[2603.08100v1](https://arxiv.org/abs/2603.08100) · [PDF](https://arxiv.org/pdf/2603.08100.pdf)  
**作者**：Chengchao Shen  

**一句话要点**：提出自适应MLP剪枝方法以减少大型视觉Transformer的参数和计算量

**关键词**：视觉Transformer, 模型剪枝, MLP模块, 自适应压缩, 参数减少, 计算效率

## 3 点简述
- 大型视觉Transformer参数冗余，MLP模块占主导，导致计算和内存需求高。
- 采用泰勒方法和标签无关信息熵准则评估MLP神经元重要性，自适应剪枝避免预设压缩率。
- 在CLIP和DINOv2等模型上实现约40%参数和FLOPs减少，性能损失小，优于其他剪枝方法。

## 摘要（原文）

> Large vision transformers present impressive scalability, as their performance can be well improved with increased model capacity. Nevertheless, their cumbersome parameters results in exorbitant computational and memory demands. By analyzing prevalent transformer structures, we find that multilayer perceptron (MLP) modules constitute the largest share of the model's parameters. In this paper, we propose an Adaptive MLP Pruning (AMP) method to substantially reduce the parameters of large vision transformers without obvious performance degradation. First, we adopt Taylor based method to evaluate neuron importance of MLP. However, the importance computation using one-hot cross entropy loss ignores the potential predictions on other categories, thus degrading the quality of the evaluated importance scores. To address this issue, we introduce label-free information entropy criterion to fully model the predictions of the original model for more accurate importance evaluation. Second, we rank the hidden neurons of MLP by the above importance scores and apply binary search algorithm to adaptively prune the ranked neurons according to the redundancy of different MLP modules, thereby avoiding the predefined compression ratio. Experimental results on several state-of-the-art large vision transformers, including CLIP and DINOv2, demonstrate that our method achieves roughly 40\% parameter and FLOPs reduction in a near lossless manner. Moreover, when the models are not finetuned after pruning, our method outperforms other pruning methods by significantly large margin. The source code and trained weights are available at https://github.com/visresearch/AMP.

