terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.7.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "orkuz-rg" {
  name     = "orkuz-rg"
  location = "eastasia"
}

resource "azurerm_kubernetes_cluster" "aks-orkuz" {
  name                = "aks-orkuz"
  location            = azurerm_resource_group.orkuz-rg.location
  resource_group_name = azurerm_resource_group.orkuz-rg.name
  dns_prefix          = "orkuz-2022L"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_B2s"

    tags = {
      pool = "Standard_B2s-2x"
    }
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_kubernetes_cluster_node_pool" "additional" {
  name                  = "additional"
  kubernetes_cluster_id = azurerm_kubernetes_cluster.aks-orkuz.id
  vm_size               = "Standard_F2s_v2"
  node_count            = 1

  tags = {
    pool = "Standard_F2s_v2-1x"
  }
}

resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "az aks get-credentials --resource-group ${azurerm_resource_group.orkuz-rg.name} --name ${azurerm_kubernetes_cluster.aks-orkuz.name} --overwrite-existing"
  }
}
